from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('about/', views.about, name='dashboard-about'),
    path('subjects/', views.subjects, name='subjects'),
]