# Generated by Django 4.1.7 on 2023-06-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_trafficaccident_date_occurred'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficAccident_111',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255)),
                ('village', models.CharField(blank=True, max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('section', models.CharField(blank=True, max_length=255)),
                ('crossroad', models.CharField(blank=True, max_length=255)),
                ('death_toll', models.IntegerField()),
                ('injured_toll', models.IntegerField()),
                ('weather_desc', models.CharField(max_length=255)),
                ('light_desc', models.CharField(max_length=255)),
                ('road_type_desc', models.CharField(max_length=255)),
                ('accident_location_desc', models.CharField(max_length=255)),
                ('road_surface_condition_desc', models.CharField(max_length=255)),
                ('road_surface_defect_desc', models.CharField(max_length=255)),
                ('obstacle_desc', models.CharField(max_length=255)),
                ('traffic_sign_desc', models.CharField(max_length=255)),
                ('div_facility_desc', models.CharField(max_length=255)),
                ('expressway_desc', models.CharField(max_length=255)),
                ('expressway_slow_fast_lane_desc', models.CharField(max_length=255)),
                ('road_side_line_desc', models.CharField(max_length=255)),
                ('accident_type_and_form_desc', models.CharField(max_length=255)),
                ('surveillance_tape', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='TrafficAccident',
            new_name='TrafficAccident_110',
        ),
    ]
