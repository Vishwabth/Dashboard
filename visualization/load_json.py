import json
from visualization.models import DataPoint

with open(r'C:\Users\vishw\Desktop\dashboard\visualization\jsondata.json', 'r') as file:  # Correct file path
    data = json.load(file)

for item in data:
    DataPoint.objects.create(
        intensity=item.get('intensity', 0),
        likelihood=item.get('likelihood', 0),
        relevance=item.get('relevance', 0),
        year=item.get('year', 0),
        country=item.get('country', ''),
        topics=item.get('topics', ''),
        region=item.get('region', ''),
        city=item.get('city', '')
    )

print("Data loaded successfully!")
