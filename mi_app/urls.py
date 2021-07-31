from django.urls import path     
from . import views


urlpatterns = [
    path('', views.root),
    path('blogs', views.index),                        # solo coincidiría con localhost:8000/bears
    path('blogs/new', views.new),       # solo coincidiría con localhost:8000/bears/23
    path('blogs/create', views.create),       # solo coincidiría con localhost:8000/bears/pooh/poke
    path('blogs/json', views.json),         
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
   	path('blogs/<int:number>/delete', views.destroy),
    path('home', views.home)
]
