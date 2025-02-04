# Generated by Django 4.2.15 on 2024-10-09 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0076_rename_date_of_issue_achievements_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=100)),
                ('interview_date', models.DateTimeField()),
                ('round', models.CharField(choices=[('Technical Round 1', 'Technical Round 1'), ('Technical Round 2', 'Technical Round 2'), ('HR Round', 'HR Round')], max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Selected', 'Selected'), ('Rejected', 'Rejected')], default='Pending', max_length=50)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.jobrole')),
            ],
        ),
    ]
