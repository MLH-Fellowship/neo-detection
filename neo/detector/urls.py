  
from django.urls import path
from .views import home

app_name = 'detector'

urlpatterns = [
    path("", home, name="home"),
]