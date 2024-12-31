import csv
import os
from django.core.management.base import BaseCommand
from whisky.models import Whisky
from django.conf import settings

class Command(BaseCommand):
    help = 'Load whisky data from CSV file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'data/whisky_data.csv')
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name_parts = row['name'].rsplit(',',1)
                name = name_parts[0]
                abv = name_parts[1].strip().rstrip('%') if len(name_parts) > 1 else ''

                try:
                    price = float(row['price'].replace(',', ''))
                except ValueError:
                    price = 0.0  # 혹시라도 변환에 실패하면 기본값으로 0.0을 사용
                Whisky.objects.update_or_create(
                    name=row['name'],
                    defaults={
                        'category': row['category'],
                        'abv': abv,
                        'rating': row['rating'],
                        'price': price,
                        'currency': row['currency'],
                        'description': row['description'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded whisky data'))

