# Generated by Django 4.2.1 on 2023-06-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management_app', '0003_remove_events_members_event_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
