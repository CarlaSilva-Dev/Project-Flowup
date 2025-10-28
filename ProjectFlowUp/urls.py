# ProjectFlowUp/urls.py

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    # AQUI MUDOU DE 'tarefas.urls' PARA 'tasks.urls'
    path('', include('tasks.urls')), 
    path('admin/', admin.site.urls),
]