from django.urls import path
from . import views

urlpatterns = [
    path('', views.plants_list, name='plants_list'),
    path('plants/<int:pk>', views.plant_detail, name='plant_detail'),
    path('plants/new', views.plant_create, name='plant_create'),

]
