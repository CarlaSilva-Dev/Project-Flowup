# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='lista_tarefas'), 
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('<int:pk>/', views.gerenciar_tarefa, name='gerenciar_tarefa'),
]