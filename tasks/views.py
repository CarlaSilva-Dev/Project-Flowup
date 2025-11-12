from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tarefa
import json


# Página inicial
def inicio(request):
    return render(request, 'tasks/inicio.html')


# Página Tarefas
def tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-id')
    return render(request, 'tasks/tarefas.html', {'tarefas': tarefas})

# Adicionar tarefa
@csrf_exempt
def add_tarefa(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Tarefa.objects.create(titulo=data['titulo'])
        return JsonResponse({'status': 'ok'})

# Excluir tarefa
def delete_tarefa(request, id):
    Tarefa.objects.filter(id=id).delete()
    return JsonResponse({'status': 'ok'})
