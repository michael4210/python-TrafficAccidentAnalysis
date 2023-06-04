from django.db import models

# Create your models here.


# class Accident(models.Model):
#     RANKING = models.IntegerField()
#     CAUSE = models.CharField(max_length=255)
#     COUNT = models.IntegerField()
#     DEATH_COUNT = models.IntegerField()
#     INJURED_COUNT = models.IntegerField()
#     CASUALTIES_COUNT = models.IntegerField()
#     CATEGORY = models.CharField(max_length=50)
class MotorcycleAccident(models.Model):
    ranking = models.IntegerField()
    cause = models.CharField(max_length=255)
    count = models.IntegerField()
    death_count = models.IntegerField()
    injured_count = models.IntegerField()
    casualties_count = models.IntegerField()


class SmallCarAccident(models.Model):
    ranking = models.IntegerField()
    cause = models.CharField(max_length=255)
    count = models.IntegerField()
    death_count = models.IntegerField()
    injured_count = models.IntegerField()
    casualties_count = models.IntegerField()


class BicycleAccident(models.Model):
    ranking = models.IntegerField()
    cause = models.CharField(max_length=255)
    count = models.IntegerField()
    death_count = models.IntegerField()
    injured_count = models.IntegerField()
    casualties_count = models.IntegerField()


class PedestrianAccident(models.Model):
    ranking = models.IntegerField()
    cause = models.CharField(max_length=255)
    count = models.IntegerField()
    death_count = models.IntegerField()
    injured_count = models.IntegerField()
    casualties_count = models.IntegerField()

class TrafficAccident_110(models.Model):
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255)
    section = models.CharField(max_length=255, blank=True)
    crossroad = models.CharField(max_length=255, blank=True)
    death_toll = models.IntegerField()
    injured_toll = models.IntegerField()
    weather_desc = models.CharField(max_length=255)
    light_desc = models.CharField(max_length=255)
    road_type_desc = models.CharField(max_length=255)
    accident_location_desc = models.CharField(max_length=255)
    road_surface_condition_desc = models.CharField(max_length=255)
    road_surface_defect_desc = models.CharField(max_length=255)
    obstacle_desc = models.CharField(max_length=255)
    traffic_sign_desc = models.CharField(max_length=255)
    div_facility_desc = models.CharField(max_length=255)
    expressway_desc = models.CharField(max_length=255)
    expressway_slow_fast_lane_desc = models.CharField(max_length=255)
    road_side_line_desc = models.CharField(max_length=255)
    accident_type_and_form_desc = models.CharField(max_length=255)
    surveillance_tape = models.BooleanField()

class TrafficAccident_111(models.Model):
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255)
    section = models.CharField(max_length=255, blank=True)
    crossroad = models.CharField(max_length=255, blank=True)
    death_toll = models.IntegerField()
    injured_toll = models.IntegerField()
    weather_desc = models.CharField(max_length=255)
    light_desc = models.CharField(max_length=255)
    road_type_desc = models.CharField(max_length=255)
    accident_location_desc = models.CharField(max_length=255)
    road_surface_condition_desc = models.CharField(max_length=255)
    road_surface_defect_desc = models.CharField(max_length=255)
    obstacle_desc = models.CharField(max_length=255)
    traffic_sign_desc = models.CharField(max_length=255)
    div_facility_desc = models.CharField(max_length=255)
    expressway_desc = models.CharField(max_length=255)
    expressway_slow_fast_lane_desc = models.CharField(max_length=255)
    road_side_line_desc = models.CharField(max_length=255)
    accident_type_and_form_desc = models.CharField(max_length=255)
    surveillance_tape = models.BooleanField()