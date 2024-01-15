from django.contrib import admin
from django.urls import path

from scraping_service.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
]
