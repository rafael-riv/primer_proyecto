from django.urls import path     
from . import views


urlpatterns = [
    path('home', views.index),
    path('claves',views.random),
    #path('reset',views.reset)
    path('login',views.login)
    ]