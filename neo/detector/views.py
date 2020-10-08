import os
import json
import requests
from django.shortcuts import render

# Create your views here.
def home(request):
    is_cached = ('neodata' in request.session)
    # Refresh cache every 15 minutes once it expires
    request.session.set_expiry(60 * 15)

    if not is_cached:
        params = dict(api_key=os.getenv('NASA_API_KEY'), size=10, page=5)
        response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse', params)
        request.session['neodata'] = response.json()

    neodata = request.session['neodata']

    return render(request, "detector/home.html", { "neos": neodata['near_earth_objects'], 'is_cached': is_cached })