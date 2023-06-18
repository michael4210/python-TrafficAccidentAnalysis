
import os
import django
import json
from django.core.management import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teamProject.settings')
django.setup()

from website.models import MotorcycleAccident, SmallCarAccident, BicycleAccident, PedestrianAccident,TrafficAccident_110,TrafficAccident_111

MotorcycleAccident.objects.all().delete()
SmallCarAccident.objects.all().delete()
BicycleAccident.objects.all().delete()
PedestrianAccident.objects.all().delete()
TrafficAccident_110.objects.all().delete()
TrafficAccident_111.objects.all().delete()
class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('機車事故統計111年.json',encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                item = {k.lower(): v for k, v in item.items()}
                MotorcycleAccident.objects.create(**item)

        with open('小型車事故統計111年.json',encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                item = {k.lower(): v for k, v in item.items()}
                SmallCarAccident.objects.create(**item)

        with open('自行車事故統計111年.json',encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                item = {k.lower(): v for k, v in item.items()}
                BicycleAccident.objects.create(**item)

        with open('行人事故統計111年.json',encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                item = {k.lower(): v for k, v in item.items()}
                PedestrianAccident.objects.create(**item)
        with open('110年高雄交通事故(缺1.4.8月).json',encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                item['surveillance_tape'] = True if item['surveillance_tape'] == 'Y' else False
                item = {k.lower(): v for k, v in item.items()}
                try:
                    TrafficAccident_110.objects.create(**item)
                except Exception as e:
                    print(f"Error creating object: {e}")
                    print(f"Failed item: {item}")
        with open('111年高雄交通事故.json',encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                item['surveillance_tape'] = True if item['surveillance_tape'] == 'Y' else False
                item = {k.lower(): v for k, v in item.items()}
                try:
                    TrafficAccident_111.objects.create(**item)
                except Exception as e:
                    print(f"Error creating object: {e}")
                    print(f"Failed item: {item}")