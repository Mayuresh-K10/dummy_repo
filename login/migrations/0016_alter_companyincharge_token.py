# Generated by Django 5.1.2 on 2024-10-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_remove_new_user_educations_new_user_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyincharge',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]