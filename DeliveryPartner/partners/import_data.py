import json
from .models import Partner


def import_data():
    json_file_path = 'pdvs.json'

    with open(json_file_path) as f:
        data = json.load(f)

    for item in data:
        partner = Partner(
            id=item['id'],
            tradingName=item['tradingName'],
            ownerName=item['ownerName'],
            document=item['document'],
            coverageArea=item['coverageArea'],
            address=item['address']
        )
        partner.save()


import_data()
