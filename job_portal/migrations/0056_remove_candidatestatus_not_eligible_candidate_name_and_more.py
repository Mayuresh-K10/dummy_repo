# Generated by Django 4.2.15 on 2024-09-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0055_message_is_primary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatestatus_not_eligible',
            name='candidate_name',
        ),
        migrations.RemoveField(
            model_name='candidatestatus_rejected',
            name='candidate_name',
        ),
        migrations.RemoveField(
            model_name='candidatestatus_selected',
            name='candidate_name',
        ),
        migrations.RemoveField(
            model_name='candidatestatus_under_review',
            name='candidate_name',
        ),
        migrations.AddField(
            model_name='candidatestatus_not_eligible',
            name='first_name',
            field=models.CharField(default='John', max_length=255),
        ),
        migrations.AddField(
            model_name='candidatestatus_not_eligible',
            name='last_name',
            field=models.CharField(default='Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='candidatestatus_rejected',
            name='first_name',
            field=models.CharField(default='John', max_length=255),
        ),
        migrations.AddField(
            model_name='candidatestatus_rejected',
            name='last_name',
            field=models.CharField(default='Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='candidatestatus_selected',
            name='first_name',
            field=models.CharField(default='John', max_length=255),
        ),
        migrations.AddField(
            model_name='candidatestatus_selected',
            name='last_name',
            field=models.CharField(default='Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='candidatestatus_under_review',
            name='first_name',
            field=models.CharField(default='John', max_length=255),
        ),
        migrations.AddField(
            model_name='candidatestatus_under_review',
            name='last_name',
            field=models.CharField(default='Doe', max_length=255),
        ),
    ]