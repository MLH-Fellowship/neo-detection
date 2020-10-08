import os
import json
import requests
# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
  response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={}'.format(os.getenv('NASA_API_KEY')))
  data = response.json()
  #print(data)
  # return render(request, "detector/home.html", {"neos": data['near_earth_objects']})
  return JsonResponse({"neos": data['near_earth_objects']}, status=200)