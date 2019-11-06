from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.plants_list, name='plants_list'),
    path('plants/<int:pk>', views.plant_detail, name='plant_detail'),
    path('plants/new', views.plant_create, name='plant_create'),
    path('plants/<int:pk>/edit', views.plant_edit, name='plant_edit'),
    path('plants/<int:pk>/delete', views.plant_delete, name='plant_delete'),
    path('login',
         auth_views.LoginView.as_view(template_name='plant_mom/login.html'),
         name='login'),
    path('logout',
         auth_views.LogoutView.as_view(template_name='plant_mom/logout.html'), name='logout'),
    path('signup', views.sign_up, name="signup"),
]
