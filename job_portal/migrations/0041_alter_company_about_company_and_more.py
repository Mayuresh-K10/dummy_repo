# Generated by Django 4.2.15 on 2024-09-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0040_company_attachment_company_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about_company',
            field=models.CharField(default='about_company', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='website_urls',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]