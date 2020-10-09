  
from django.urls import path
from .views import browse

urlpatterns = [
    path("browse/", browse, name="browse"),
]