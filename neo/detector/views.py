import os
import json
import requests
from django.shortcuts import render

# Create your views here.
def home():
  response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={}'.format(os.getenv('NASA_API_KEY')))
  data = response.json()
  print(data)
  return render("detector/home.html", {"neos": data['near_earth_objects']})