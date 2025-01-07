import json
from django.core.management.base import BaseCommand
from main.models import Institution


class Command(BaseCommand):
    help="Import external Institution JSON files data into database"

    def handle(self, *args, **kwargs):
        with open(r'/Users/abid/Downloads/main_institution.json', 'r', encoding='utf8')as file:
            data = json.load(file)
            for item in data:
                Institution.objects.create(
                    id=item['id'],
                    name=item['name'],
                    address=item['address'],
                    state=item['state_id'],
                    pincode=item['pincode'],
                    created=item['created'],
                    updated=item['updated'],
                )
        
        self.stdout.write(self.style.SUCCESS('Done'))




#/Users/abid/Downloads