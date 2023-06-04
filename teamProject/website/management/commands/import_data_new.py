import csv,os,django
from datetime import datetime
from django.core.management import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teamProject.settings')
django.setup()
from website.models import TrafficAccident_110

TrafficAccident_110.objects.all().delete()
class Command(BaseCommand):
    help = 'Import traffic accident data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the CSV file')    
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        traffic_accident_list = []
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                   
                    traffic_accident = TrafficAccident_110(                        
                        district=row[0],
                        village=row[1],
                        street=row[2],
                        section=row[3],
                        crossroad=row[4],
                        death_toll=int(row[5]),
                        injured_toll=int(row[6]),
                        weather_desc=row[7],
                        light_desc=row[8],
                        road_type_desc=row[9],
                        accident_location_desc=row[10],
                        road_surface_condition_desc=row[11],
                        road_surface_defect_desc=row[12],
                        obstacle_desc=row[13],
                        traffic_sign_desc=row[14],
                        div_facility_desc=row[15],
                        expressway_desc=row[16],
                        expressway_slow_fast_lane_desc=row[17],
                        road_side_line_desc=row[18],
                        accident_type_and_form_desc=row[19],
                        surveillance_tape=row[20] == 'Y',
                    )
                    traffic_accident_list.append(traffic_accident)
                except Exception as e:
                    print(e)
                    raise
                # traffic_accident.save()
                 # Add the object to the list instead of saving it directly
            TrafficAccident_110.objects.bulk_create(traffic_accident_list) # Save all the objects in the list at once                   
