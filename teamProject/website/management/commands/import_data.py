
import os
import django
import json
from django.core.management import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teamProject.settings')
django.setup()

from website.models import MotorcycleAccident, SmallCarAccident, BicycleAccident, PedestrianAccident

MotorcycleAccident.objects.all().delete()
SmallCarAccident.objects.all().delete()
BicycleAccident.objects.all().delete()
PedestrianAccident.objects.all().delete()

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
