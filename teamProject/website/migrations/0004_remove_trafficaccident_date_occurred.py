# Generated by Django 4.1.7 on 2023-06-04 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_trafficaccident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficaccident',
            name='date_occurred',
        ),
    ]
