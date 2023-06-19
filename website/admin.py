from django.contrib import admin
from website import models

# Register your models here.

admin.site.register(models.MotorcycleAccident)
admin.site.register(models.SmallCarAccident)
admin.site.register(models.BicycleAccident)
admin.site.register(models.PedestrianAccident)
admin.site.register(models.TrafficAccident_110)
admin.site.register(models.TrafficAccident_111)