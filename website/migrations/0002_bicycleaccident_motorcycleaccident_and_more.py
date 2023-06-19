# Generated by Django 4.1.7 on 2023-05-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BicycleAccident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('cause', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('death_count', models.IntegerField()),
                ('injured_count', models.IntegerField()),
                ('casualties_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MotorcycleAccident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('cause', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('death_count', models.IntegerField()),
                ('injured_count', models.IntegerField()),
                ('casualties_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PedestrianAccident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('cause', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('death_count', models.IntegerField()),
                ('injured_count', models.IntegerField()),
                ('casualties_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SmallCarAccident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('cause', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('death_count', models.IntegerField()),
                ('injured_count', models.IntegerField()),
                ('casualties_count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Accident',
        ),
    ]
