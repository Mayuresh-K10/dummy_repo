# Generated by Django 4.2.15 on 2024-09-26 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_portal', '0061_remove_usersubscription_current_plan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('standard', 'Standard'), ('gold', 'Gold'), ('diamond', 'Diamond')], max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('job_postings', models.PositiveIntegerField(default=0)),
                ('featured_jobs', models.PositiveIntegerField(default=0)),
                ('job_duration_days', models.PositiveIntegerField(default=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renewal_date', models.DateField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('plan', models.CharField(default='Standard', max_length=15)),
                ('current_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_portal.membershipplan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]