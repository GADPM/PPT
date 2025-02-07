# PPT_app/urls.py
from django.urls import path
from .views import menu, play

urlpatterns = [
    path('', menu, name='menu'),
    path('play/', play, name='play'),
]
