from django.shortcuts import render
from django.db.models import Sum,F
from collections import defaultdict
from .models import MotorcycleAccident, SmallCarAccident, BicycleAccident, PedestrianAccident,TrafficAccident_110,TrafficAccident_111


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
def traffic_accidents_110(request):
    # street_data = TrafficAccident_110.objects.values('street').annotate(
    #     total_injured=Sum('injured_toll'),
    #     total_death=Sum('death_toll')
    # ).order_by('-total_injured', '-total_death')
    traffic_accidents = TrafficAccident_110.objects.all()
    context = {
        # 'street_data': street_data,
        'traffic_accidents': traffic_accidents,
    }
    
    return render(request, 'traffic_accident_110.html',context )


def traffic_accidents_111(request):
    traffic_accidents = TrafficAccident_111.objects.all()
    return render(request, 'traffic_accident_111.html',{'traffic_accidents': traffic_accidents} )

def analysis(request):

   # Get all traffic accidents from both models
    traffic_accidents_110 = TrafficAccident_110.objects.values('street').annotate(
        total_casualties=Sum('death_toll')+Sum('injured_toll')
    )
    traffic_accidents_111 = TrafficAccident_111.objects.values('street').annotate(
        total_casualties=Sum('death_toll')+Sum('injured_toll')
    )

    # Combine the two QuerySets
    combined_accidents = list(traffic_accidents_110) + list(traffic_accidents_111)

    # Initialize a defaultdict to store the total casualties for each street
    street_casualties = defaultdict(int)

    # Iterate over the combined data, adding the casualties for each street
    for accident in combined_accidents:
        street_casualties[accident['street']] += accident['total_casualties']

    # Convert the defaultdict to a list of tuples and sort it by casualties
    street_casualties = sorted(street_casualties.items(), key=lambda x: x[1], reverse=True)

    # Pass the sorted data to the template
    context = {'street_casualties': street_casualties}
    return render(request, 'analysis.html', context)

from itertools import chain
def conditions_analysis(request):
    conditions = ['weather_desc', 'light_desc', 'road_surface_condition_desc', 'road_type_desc', 'traffic_sign_desc']
    condition_casualties = {}

    for condition in conditions:
        # 分別對兩個年份的數據進行統計
        condition_data_110 = TrafficAccident_110.objects.values(condition).annotate(
            total_casualties=Sum('injured_toll') + Sum('death_toll')
        ).values(condition, 'total_casualties')

        condition_data_111 = TrafficAccident_111.objects.values(condition).annotate(
            total_casualties=Sum('injured_toll') + Sum('death_toll')
        ).values(condition, 'total_casualties')

        # 合併兩個年份的數據
        combined_data = list(chain(condition_data_110, condition_data_111))

        # 手動對每種條件的傷亡人數進行加總
        condition_casualty_dict = {}
        for item in combined_data:
            if item[condition] in condition_casualty_dict:
                condition_casualty_dict[item[condition]] += item['total_casualties']
            else:
                condition_casualty_dict[item[condition]] = item['total_casualties']

        condition_casualties[condition] = sorted(condition_casualty_dict.items(), key=lambda x: x[1], reverse=True)

    context = {
        'condition_casualties': condition_casualties,
    }

    return render(request, 'conditions_analysis.html', context)
    # conditions = ['weather_desc', 'light_desc', 'road_surface_condition_desc', 'road_type_desc', 'traffic_sign_desc']
    # condition_casualties = {}

    # for condition in conditions:
    #     condition_data_110 = TrafficAccident_110.objects.values(condition).exclude(**{condition: ''}).annotate(
    #         total_casualties=Sum('injured_toll') + Sum('death_toll')
    #     ).order_by('-total_casualties')
    #     condition_data_111 = TrafficAccident_111.objects.values(condition).exclude(**{condition: ''}).annotate(
    #         total_casualties=Sum('injured_toll') + Sum('death_toll')
    #     ).order_by('-total_casualties')

    #     # convert each accident into a dictionary with the keys 'condition' and 'total_casualties'
    #     condition_casualties[condition] = [
    #         {'condition': item[condition], 'total_casualties': item['total_casualties']}
    #         for item in list(condition_data_110) + list(condition_data_111)
    #     ]
        
    # context = {
    #     'condition_casualties': condition_casualties,
    # }

    # return render(request, 'conditions_analysis.html', context)
    # traffic_accidents = list(TrafficAccident_110.objects.all()) + list(TrafficAccident_111.objects.all())