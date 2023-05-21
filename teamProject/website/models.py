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
