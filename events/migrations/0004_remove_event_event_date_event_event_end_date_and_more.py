# Generated by Django 4.2 on 2023-04-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.AddField(
            model_name='event',
            name='event_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start_date',
            field=models.DateTimeField(null=True),
        ),
    ]