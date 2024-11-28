from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_inicial, name='menu_inicial'),
    path('historia/', views.historia, name='historia'),
    path('creditos/', views.creditos, name='creditos'),
    path('', views.index, name='index'),  # Página onde o usuário escolhe a jogada
    path('jogar/', views.jogar, name='jogar'),  # Página para mostrar o resultado
]
