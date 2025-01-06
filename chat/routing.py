from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<str:token>/<str:user_model>/<str:user_email>/", consumers.ChatConsumer.as_asgi()),
    path('ws/notifications/<str:token>/', consumers.NotificationConsumer.as_asgi()),
]
