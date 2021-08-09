from django.urls import path     
from . import views


urlpatterns = [
    path('home', views.index),
    path('process_money' , views.gold)
    ]