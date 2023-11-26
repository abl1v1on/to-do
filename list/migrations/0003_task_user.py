# Generated by Django 4.2.7 on 2023-11-25 19:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
