# Generated by Django 3.0.5 on 2020-05-21 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0014_auto_20200521_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewsubmissionscore',
            name='reviewed_by',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
