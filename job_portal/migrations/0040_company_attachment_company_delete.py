# Generated by Django 4.2.15 on 2024-09-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0039_remove_company_country_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Attachment',
            field=models.FileField(default='Unknown', upload_to='attachments/'),
        ),
        migrations.AddField(
            model_name='company',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]