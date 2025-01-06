# Generated by Django 5.1.4 on 2025-01-02 10:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0118_alter_education_end_date_alter_education_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='publications',
            name='publisher',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='publications',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='publications',
            name='title',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]