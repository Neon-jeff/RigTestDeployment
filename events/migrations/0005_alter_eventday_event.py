# Generated by Django 4.2 on 2023-04-15 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_event_event_date_event_event_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventday',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events.event'),
        ),
    ]
