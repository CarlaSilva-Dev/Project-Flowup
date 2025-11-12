from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('add/', views.add_tarefa, name='add_tarefa'),
    path('delete/<int:id>/', views.delete_tarefa, name='delete_tarefa'),
]
