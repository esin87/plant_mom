from django.urls import path
from . import views

urlpatterns = [
    path('', views.plants_list, name='plants_list'),
    path('plants/<int:pk>', views.plant_detail, name='plant_detail'),
    path('plants/new', views.plant_create, name='plant_create'),
    path('plants/<int:pk>/edit', views.plant_edit, name='plant_edit'),
    path('plants/<int:pk>/delete', views.plant_delete, name='plant_delete'),

]
