# Generated by Django 4.2.14 on 2024-08-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0015_alter_job_job_title_alter_job_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]