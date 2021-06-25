from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('s.urls')),
]
