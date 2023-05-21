from django.shortcuts import render
from .models import MotorcycleAccident, SmallCarAccident, BicycleAccident, PedestrianAccident


def all_accidents(request):
    motorcycle_accidents = MotorcycleAccident.objects.all()
    small_car_accidents = SmallCarAccident.objects.all()
    bicycle_accidents = BicycleAccident.objects.all()
    pedestrian_accidents = PedestrianAccident.objects.all()

    context = {
        'motorcycle_accidents': motorcycle_accidents,
        'small_car_accidents': small_car_accidents,
        'bicycle_accidents': bicycle_accidents,
        'pedestrian_accidents': pedestrian_accidents,
    }

    return render(request, 'accident.html', context)
