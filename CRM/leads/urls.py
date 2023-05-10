from django.contrib import admin
from django.urls import path
from leads import views

app_name = 'leads'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('<int:pk>/', views.lead_detail, name='lead_detail'),
    path('create/', views.lead_create, name='lead_create'),
    path('<int:pk>/update/', views.lead_update, name='lead_update'),
    path('<int:pk>/delete/', views.lead_delete, name='lead_delete'),


]
