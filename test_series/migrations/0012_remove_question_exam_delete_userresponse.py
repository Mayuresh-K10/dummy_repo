# Generated by Django 4.2.11 on 2024-07-30 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_series', '0011_question_userresponse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='exam',
        ),
        migrations.DeleteModel(
            name='UserResponse',
        ),
    ]