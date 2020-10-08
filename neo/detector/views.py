import os
import json
import requests
import time
from django.shortcuts import render

# Create your views here.
def home(request):
    is_cached = ('neodata' in request.session)
    # Refresh cache every 15 minutes once it expires
    is_expired = ('cache_time' in request.session and time.time() - request.session['cache_time'] >= 60 * 15)

    if not is_cached or is_expired:
        params = dict(api_key=os.getenv('NASA_API_KEY'), size=10, page=5)
        response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse', params)
        request.session['neodata'] = response.json()
        request.session['cache_time'] = time.time()

    neodata = request.session['neodata']

    return render(request, "detector/home.html", { "neos": neodata['near_earth_objects'], 'is_cached': is_cached })