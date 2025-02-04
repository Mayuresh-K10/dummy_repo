# Generated by Django 5.1.4 on 2025-01-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0120_alter_publications_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='publisher',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='achievements',
            name='title',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='certification',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(default='No description'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='job_title',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='No description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_link',
            field=models.TextField(default=list),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='Untitled Project', max_length=100),
        ),
        migrations.AlterField(
            model_name='reference',
            name='contact_info',
            field=models.CharField(default='Not provided', max_length=100),
        ),
        migrations.AlterField(
            model_name='reference',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='reference',
            name='relationship',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
