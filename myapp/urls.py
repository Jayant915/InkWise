from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example: index.html
    path('about/', views.about, name='about'),  # Example: about.html
    path('services/', views.services, name='services'), # Example: services.html
    path('pricing/', views.pricing, name='pricing'), # Example: pricing.html
    path('contact/', views.contact, name='contact'), # Example: contact.html
    path('team/', views.team, name='team'), # Example: team.html
]