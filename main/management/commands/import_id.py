import json
from django.core.management.base import BaseCommand
from main.models import InstitutionDetails


class Command(BaseCommand):
    help="Import external Institution Details JSON files data into database"

    def handle(self, *args, **kwargs):
        with open(r'/Users/abid/Downloads/id_final.json', 'r', encoding='utf8')as file:
            data = json.load(file)
            for item in data:
                InstitutionDetails.objects.create(
                    id=item['id'],
                    moh_name=item['moh_name'],
                    moh_phone=item['moh_phone'],
                    safir_name=item['safir_name'],
                    safir_phone=item['safir_phone'],
                    safir_aadhar=item['safir_aadhar'],
                    taalim=item['taalim'],
                    total_students=item['total_students'],
                    res_students=item['res_students'],
                    total_teachers=item['total_teachers'],
                    donation_day=item['donation_day'],
                    serial_no=item['serial_no'],
                    halka_code=item['halka_code'],
                    ijazat_status=item['ijazat_status'],
                    next_donation_year=item['next_donation_year'],
                    comments=item['comments'],
                    safir_photo=item['safir_photo'],
                    institution=item['institution_id'],
                    year=item['year_id'],
                    created=item['created'],
                    updated=item['updated'],
                )
        
        self.stdout.write(self.style.SUCCESS('Done'))
        # print(data)



#/Users/abid/Downloads