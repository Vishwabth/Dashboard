import json
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from collections import defaultdict
from .models import DataPoint
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from django.http import JsonResponse


def get_data(request):
    json_file_path = os.path.join(settings.BASE_DIR, "visualization", "jsondata.json")
    if not os.path.exists(json_file_path):
        return JsonResponse({"error": "JSON file not found"}, status=404)
    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    def safe_strip(value):
        return str(value).strip() if isinstance(value, str) else str(value)
    total_records = len(data)
    unique_sectors = len(set(safe_strip(item.get("sector", "Unknown")) for item in data if "sector" in item))
    unique_countries = len(set(safe_strip(item.get("country", "Unknown")) for item in data if "country" in item))
    latest_insights = [
        {
            "title": item.get("title", "No Title"),
            "sector": safe_strip(item.get("sector", "Unknown")),
            "country": safe_strip(item.get("country", "Unknown")),
            "published": item.get("published", "N/A"),
            "url": item.get("url", "#"),
        }
        for item in data if item.get("title")
    ][:100]
    sector_counts = defaultdict(int)
    for item in data:
        sector = safe_strip(item.get("sector", "Unknown"))
        if sector:
            sector_counts[sector] += 1
    topic_counts = defaultdict(int)
    for item in data:
        topic = safe_strip(item.get("topic", "Unknown"))
        if topic:
            topic_counts[topic] += 1
    country_counts = defaultdict(int)
    for item in data:
        country = safe_strip(item.get("country", "Unknown"))
        if country:
            country_counts[country] += 1
    intensity_counts = defaultdict(int)
    for item in data:
        intensity = item.get("intensity", 0)
        if isinstance(intensity, (int, float)):
            intensity_counts[str(intensity)] += 1
    intensity_labels = sorted(intensity_counts.keys())
    intensity_values = [intensity_counts[key] for key in intensity_labels]
    likelihood_counts = defaultdict(int)
    for item in data:
        likelihood = item.get("likelihood", 0)
        if isinstance(likelihood, (int, float)):
            likelihood_counts[str(likelihood)] += 1

    likelihood_labels = sorted(likelihood_counts.keys())
    likelihood_values = [likelihood_counts[key] for key in likelihood_labels]
    relevance_counts = defaultdict(int)
    for item in data:
        relevance = item.get("relevance", 0)
        if isinstance(relevance, (int, float)):
            relevance_counts[str(relevance)] += 1
    relevance_labels = sorted(relevance_counts.keys())
    relevance_values = [relevance_counts[key] for key in relevance_labels]
    country_counts = defaultdict(int)
    for item in data:
        country = safe_strip(item.get("country", "Unknown"))
        if country:
            country_counts[country] += 1

    country_labels = list(country_counts.keys())
    country_values = list(country_counts.values())
    region_counts = defaultdict(int)
    for item in data:
        region = safe_strip(item.get("region", "Unknown"))
        if region:
            region_counts[region] += 1
    region_labels = list(region_counts.keys())
    region_values = list(region_counts.values())
    city_counts = defaultdict(int)
    for item in data:
        city = safe_strip(item.get("city", "Unknown"))
        if city:
            city_counts[city] += 1
    city_labels = list(city_counts.keys())
    city_values = list(city_counts.values())
    context = {
        "total_records": total_records,
        "unique_sectors": unique_sectors,
        "unique_countries": unique_countries,
        "latest_insights": latest_insights,
        "sector_labels": json.dumps(list(sector_counts.keys())),
        "sector_counts": json.dumps(list(sector_counts.values())),
        "topic_labels": json.dumps(list(topic_counts.keys())),
        "topic_counts": json.dumps(list(topic_counts.values())),
        "country_labels": json.dumps(list(country_counts.keys())),
        "country_counts": json.dumps(list(country_counts.values())),
        "intensity_labels": json.dumps(intensity_labels),
        "intensity_values": json.dumps(intensity_values),
        "likelihood_labels": json.dumps(likelihood_labels),
        "likelihood_values": json.dumps(likelihood_values),
        "relevance_labels": json.dumps(relevance_labels),
        "relevance_values": json.dumps(relevance_values),
        "country_labels": json.dumps(country_labels),
        "country_values": json.dumps(country_values),
        "region_labels": json.dumps(region_labels),
        "region_counts": json.dumps(region_values),
        "city_labels": json.dumps(city_labels),
        "city_counts": json.dumps(city_values),
    }
    filters = {
        "sectors": DataPoint.objects.values_list("sector", flat=True).distinct(),
        "end_years": DataPoint.objects.values_list("end_year", flat=True).distinct(),
        "topic_name": DataPoint.objects.values_list("topic", flat=True).distinct(),
        "region_name": DataPoint.objects.values_list("region", flat=True).distinct(),
        "pestles": DataPoint.objects.values_list("pestle", flat=True).distinct(),
        "sources": DataPoint.objects.values_list("source", flat=True).distinct(),
        #"swots": DataPoint.objects.values_list("swot", flat=True).distinct(),
        "countries": DataPoint.objects.values_list("country", flat=True).distinct(),
    }
    

    return render(request, "index.html", context)

def index(request):
    return render(request, "index.html")
@csrf_exempt
def filter_data(request):
    json_file_path = os.path.join(settings.BASE_DIR, "visualization", "jsondata.json")
    if not os.path.exists(json_file_path):
        return JsonResponse({"error": "JSON file not found"}, status=404)
    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)    
        filters = json.loads(request.body)  
        def safe_strip(value):
            if value is None:
                return ""
            return str(value).strip().lower() if isinstance(value, str) else str(value).lower()
        filtered_data = data
        if filters.get("sector"):
            filtered_data = [item for item in filtered_data if safe_strip(filters["sector"]) in safe_strip(item.get("sector", ""))]
            
        if filters.get("country"):
            filtered_data = [item for item in filtered_data if safe_strip(filters["country"]) in safe_strip(item.get("country", ""))]
            
        if filters.get("topic"):
            filtered_data = [item for item in filtered_data if safe_strip(filters["topic"]) in safe_strip(item.get("topic", ""))]
            
        if filters.get("region"):
            filtered_data = [item for item in filtered_data if safe_strip(filters["region"]) in safe_strip(item.get("region", ""))]
            
        if filters.get("pestle"):
            filtered_data = [item for item in filtered_data if safe_strip(filters["pestle"]) in safe_strip(item.get("pestle", ""))]
            
        if filters.get("source"):
            filtered_data = [item for item in filtered_data if safe_strip(filters["source"]) in safe_strip(item.get("source", ""))]

        intensity_counts = {}
        likelihood_counts = {}
        relevance_counts = {}
        country_counts = {}
        region_counts = {} 
        topic_counts = {} 

        for item in filtered_data:
            intensity = item.get("intensity", 0)
            if isinstance(intensity, (int, float)):
                intensity_counts[str(intensity)] = intensity_counts.get(str(intensity), 0) + 1
            likelihood = item.get("likelihood", 0)
            if isinstance(likelihood, (int, float)):
                likelihood_counts[str(likelihood)] = likelihood_counts.get(str(likelihood), 0) + 1
            relevance = item.get("relevance", 0)
            if isinstance(relevance, (int, float)):
                relevance_counts[str(relevance)] = relevance_counts.get(str(relevance), 0) + 1
            country = safe_strip(item.get("country", "Unknown"))
            country_counts[country] = country_counts.get(country, 0) + 1
            region = safe_strip(item.get("region", "Unknown"))
            region_counts[region] = region_counts.get(region, 0) + 1
            topic = safe_strip(item.get("topic", "Unknown"))
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

        intensity_labels = sorted(intensity_counts.keys())
        intensity_values = [intensity_counts[key] for key in intensity_labels]

        likelihood_labels = sorted(likelihood_counts.keys())
        likelihood_values = [likelihood_counts[key] for key in likelihood_labels]

        relevance_labels = sorted(relevance_counts.keys())
        relevance_values = [relevance_counts[key] for key in relevance_labels]

        country_labels = list(country_counts.keys())
        country_values = list(country_counts.values())

        region_labels = list(region_counts.keys())
        region_values = list(region_counts.values())

        topic_labels = list(topic_counts.keys())
        topic_values = list(topic_counts.values())

        return JsonResponse({
            "intensity_labels": intensity_labels,
            "intensity_values": intensity_values,
            "likelihood_labels": likelihood_labels,
            "likelihood_values": likelihood_values,
            "relevance_labels": relevance_labels,
            "relevance_values": relevance_values,
            "country_labels": country_labels,
            "country_values": country_values,
            "region_labels": region_labels,  
            "region_values": region_values,  
            "topic_labels": topic_labels,  
            "topic_values": topic_values,  
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    except Exception as e:
        import traceback
        traceback.print_exc() 
        return JsonResponse({"error": str(e)}, status=500)
def get_json_data(request):
    json_file_path = os.path.join(settings.BASE_DIR, "visualization", "jsondata.json")

    if not os.path.exists(json_file_path):
        return JsonResponse({"error": "JSON file not found"}, status=404)
    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)  
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)