import os
import json
import requests
from django.http import JsonResponse

# Create your views here.
def browse(request):
    if not 'neodata' in request.session:
        request.session['neodata'] = {}

    page = request.GET.get('page', 0)

    # Refresh cache every 30 minutes once it expires
    request.session.set_expiry(60 * 30)

    if not page in request.session['neodata']:
        params = dict(api_key=os.getenv('NASA_API_KEY'), size=20, page=page)
        response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse', params)
        request.session['neodata'][page] = response.json()

    neodata = request.session['neodata'][page]

    # Using JsonResponse object (an HTTPResponse subclass) to create a JSON-encoded response. Its default Content-Type header is set to application/json.
    # https://docs.djangoproject.com/en/3.1/ref/request-response/#jsonresponse-objects
    return JsonResponse({ "neodata": neodata })