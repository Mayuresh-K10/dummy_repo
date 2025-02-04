from asgiref.sync import sync_to_async # type: ignore
from django.core.exceptions import ObjectDoesNotExist # type: ignore
from django.db.models import Q # type: ignore
from .models import Message, MessageAttachment
from login.models import JobSeeker, new_user, CompanyInCharge, UniversityInCharge # type: ignore
from channels.generic.websocket import AsyncJsonWebsocketConsumer # type: ignore
from dateutil import parser # type: ignore
import json
from channels.generic.websocket import AsyncWebsocketConsumer # type: ignore


MODEL_MAPPING = {
    "JobSeeker": JobSeeker,
    "UniversityInCharge": UniversityInCharge,
    "CompanyInCharge": CompanyInCharge,
    "new_user": new_user,
}


@sync_to_async
def save_message(sender_email, recipient_email, sender_model, recipient_model, subject, content):
    return Message.objects.create(
        sender_email=sender_email,
        recipient_email=recipient_email,
        sender_model=sender_model,
        recipient_model=recipient_model,
        subject=subject,
        content=content
    )


@sync_to_async
def save_attachments(message, attachments):
    saved_attachments = []
    for attachment_data in attachments:
        try:
            attachment = MessageAttachment.objects.create(
                file=attachment_data["file"],
                original_name=attachment_data["original_name"],
                file_type=attachment_data["file_type"]
            )
            message.attachments.add(attachment)
            saved_attachments.append({
                "original_name": attachment.original_name,
                "file_url": attachment.file.url
            })
        except Exception as e:
            print(f"Error saving attachment: {e}")
    return saved_attachments


@sync_to_async
def get_user_from_db(model_class, email, token_optional=False):
    if token_optional or email:
        try:
            if hasattr(model_class, "email"):
                return model_class.objects.get(email=email)
            else:
                return model_class.objects.get(official_email=email)
        except model_class.DoesNotExist:
            raise ObjectDoesNotExist("User not found")
    raise ObjectDoesNotExist("Invalid email or token")


async def get_attachments_for_message(message):
    try:
        attachments = await sync_to_async(list)(message.attachments.all())
        return [
            {
                "original_name": attachment.original_name,
                "file_url": attachment.file.url if attachment.file and hasattr(attachment.file, 'url') else None,
                "file_type": attachment.file_type,
            }
            for attachment in attachments
        ]
    except Exception as e:
        print(f"Error retrieving attachments: {e}")
        return []


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.user_email = self.scope["url_route"]["kwargs"].get("user_email")
        self.user_model = self.scope["url_route"]["kwargs"].get("user_model")
        if not self.user_model or self.user_model not in MODEL_MAPPING:
            await self.close(code=4001)
            return

        try:
            model_class = MODEL_MAPPING[self.user_model]
            self.user = await get_user_from_db(model_class, self.user_email, token_optional=True)
        except ObjectDoesNotExist:
            await self.close(code=4002)
            return

        self.group_name = f"user_{self.user_email.replace('@', '_at_').replace('.', '_dot_')}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content):
        action = content.get("action")
        if action == "send_message":
            await self.handle_send_message(content)
        elif action == "get_messages":
            await self.handle_get_messages(content)
        else:
            await self.send_json({"error": "Invalid action"})

    async def handle_get_messages(self, content):
        recipient_email = content.get("recipient_email")
        recipient_model = content.get("recipient_model")
        sender_email = content.get("sender_email", self.user_email)
        _= content.get("sender_model", self.user_model)# Placeholder for future use
        since_timestamp = content.get("since_timestamp")

        if not recipient_email or not recipient_model:
            await self.send_json({"error": "Recipient details are required"})
            return

        try:
            messages_query = Message.objects.filter(
                Q(sender_email=sender_email, recipient_email=recipient_email) |
                Q(sender_email=recipient_email, recipient_email=sender_email)
            )
            if since_timestamp:
                since_dt = parser.parse(since_timestamp)
                messages_query = messages_query.filter(timestamp__gt=since_dt)

            # messages = await sync_to_async(list)(messages_query.order_by("timestamp"))

            await sync_to_async(messages_query.filter(is_read=False).update)(is_read=True)
            messages = await sync_to_async(list)(messages_query.order_by("timestamp"))

            message_data = []
            for message in messages:
                attachments = await get_attachments_for_message(message)
                message_data.append({
                    "id": message.id,
                    "sender_email": message.sender_email,
                    "recipient_email": message.recipient_email,
                    "sender_model": message.sender_model,
                    "recipient_model": message.recipient_model,
                    "subject": message.subject or "",
                    "content": message.content or "",
                    "timestamp": message.timestamp.isoformat(),
                    "attachments": attachments,
                })

            await self.send_json({
                "message": "Messages retrieved successfully",
                "data": message_data,
            })

        except Exception as e:
            await self.send_json({"error": f"An error occurred: {str(e)}"})

    async def handle_send_message(self, content):
        sender_email = self.user_email
        recipient_email = content.get("recipient_email")
        recipient_model = content.get("recipient_model")
        message_content = content.get("content", "").strip()
        subject = content.get("subject", "").strip()
        attachments = content.get("attachments", [])

        if not recipient_email or not recipient_model:
            await self.send_json({"error": "Recipient details are required"})
            return

        if recipient_model not in MODEL_MAPPING:
            await self.send_json({"error": "Invalid recipient model"})
            return

        try:
            recipient_class = MODEL_MAPPING[recipient_model]
            _= await self.validate_user(recipient_class, None, recipient_email, token_optional=True)# Placeholder for future use
        except ObjectDoesNotExist:
            await self.send_json({"error": "Recipient not found"})
            return

        if not message_content and not attachments:
            await self.send_json({"error": "Either content or attachments must be provided"})
            return

        try:
            message = await save_message(
                sender_email, recipient_email, self.user_model, recipient_model, subject, message_content
            )

            attachment_details = []
            if attachments:
                attachment_details = await save_attachments(message, attachments)

            response_data = {
                "id": message.id,
                "sender_email": sender_email,
                "recipient_email": recipient_email,
                "subject": subject,
                "content": message_content,
                "attachments": attachment_details,
                "timestamp": message.timestamp.isoformat(),
            }

            recipient_group = f"user_{recipient_email.replace('@', '_at_').replace('.', '_dot_')}"
            await self.channel_layer.group_send(
                recipient_group,
                {
                    "type": "chat_message",
                    "message": response_data,
                },
            )

            await self.send_json({"message": "Message sent successfully", "data": response_data})

        except Exception as e:
            await self.send_json({"error": f"An error occurred: {str(e)}"})

    async def chat_message(self, event):
        message = event["message"]
        await self.send_json({
            "action": "new_message",
            "data": message,
        })

    @staticmethod
    @sync_to_async
    def validate_user(model_class, token, email, token_optional=False):
        if token_optional or token:
            try:
                if hasattr(model_class, "email"):
                    return model_class.objects.get(email=email)
                else:
                    return model_class.objects.get(official_email=email)
            except model_class.DoesNotExist:
                raise ObjectDoesNotExist("User not found")
        raise ObjectDoesNotExist("Invalid email or token")



class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.token = self.scope['url_route']['kwargs']['token']
        self.group_name = f"notifications_{self.token}"

        # Join the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )

    async def send_notification(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({"message": message}))