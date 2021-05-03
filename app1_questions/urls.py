from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('java' , views.javaform,name="java"),
    path("q" , views.qapost , name="q"),
    path("c" , views.cpost , name="c"),
    
]