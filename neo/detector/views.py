import os
import json
import requests
from django.shortcuts import render
from django.http import JsonResponse

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

    # return render(request, "detector/home.html", { "neos": neodata['near_earth_objects'], 'is_cached': is_cached })

    # Using JsonResponse object (an HTTPResponse subclass) to create a JSON-encoded response. Its default Content-Type header is set to application/json.
    # https://docs.djangoproject.com/en/3.1/ref/request-response/#jsonresponse-objects
    return JsonResponse({"neos": neodata['near_earth_objects'], 'is_cached': is_cached})