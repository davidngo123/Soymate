from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'soymate-home'),
    path('about/', views.about, name = 'soymate-about'),
]
