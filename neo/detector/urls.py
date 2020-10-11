  
from django.urls import path
from .views import browse
from .views import news

urlpatterns = [
    path("browse/", browse, name="browse"),
    path("news/", news, name="news"),
]