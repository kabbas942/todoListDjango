from django.contrib import admin
from django.urls import path
from .views import allRecord

urlpatterns = [
    path('/all',allRecord,name="all")
]
