# Generated by Django 4.2.15 on 2024-10-14 09:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0085_remove_interview_applicant_remove_interview_job_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=255)),
                ('last_name', models.CharField(default='Doe', max_length=255)),
                ('email', models.EmailField(default='unknown@example.com', max_length=254)),
                ('phone_number', models.CharField(default='123-456-7890', max_length=15)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField(default='No cover letter provided')),
                ('applied_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('skills', models.CharField(max_length=1000)),
                ('bio', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.student')),
            ],
        ),
        migrations.CreateModel(
            name='ScreeningAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening_answers', to='job_portal.application')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='job_portal.screeningquestion')),
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
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.application')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.student')),
            ],
        ),
    ]
