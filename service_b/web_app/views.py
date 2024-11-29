import os
import logging
from django.shortcuts import render
import requests

logger = logging.getLogger(__name__)

def home_view(request):
    service_a_host = os.environ.get('SERVICE_A_HOST', 'service-a')
    service_a_url = f'http://{service_a_host}:8000/api/data/'
    try:
        response = requests.get(service_a_url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error connecting to Service A: {e}")
        data = {'items': []}
    return render(request, 'home.html', {'data': data})
