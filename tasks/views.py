from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tarefa
import json


# Página inicial
def inicio(request):
    return render(request, 'tasks/inicio.html')


# Página Tarefas - LER (READ)
def tarefas(request):
    tarefas = Tarefa.objects.all()
    total_tarefas = tarefas.count()
    tarefas_concluidas = tarefas.filter(concluida=True).count()
    porcentagem = int((tarefas_concluidas / total_tarefas * 100)) if total_tarefas > 0 else 0
    
    return render(request, 'tasks/tarefas.html', {
        'tarefas': tarefas,
        'total_tarefas': total_tarefas,
        'tarefas_concluidas': tarefas_concluidas,
        'porcentagem': porcentagem
    })


# CRIAR (CREATE) - Adicionar tarefa
@csrf_exempt
def add_tarefa(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tarefa = Tarefa.objects.create(
            titulo=data.get('titulo'),
            descricao=data.get('descricao', '')
        )
        return JsonResponse({
            'status': 'ok',
            'tarefa': {
                'id': tarefa.id,
                'titulo': tarefa.titulo,
                'descricao': tarefa.descricao,
                'concluida': tarefa.concluida
            }
        })


# ATUALIZAR (UPDATE) - Editar tarefa
@csrf_exempt
def update_tarefa(request, id):
    if request.method == 'POST':
        tarefa = get_object_or_404(Tarefa, id=id)
        data = json.loads(request.body)
        
        tarefa.titulo = data.get('titulo', tarefa.titulo)
        tarefa.descricao = data.get('descricao', tarefa.descricao)
        if 'concluida' in data:
            tarefa.concluida = data['concluida']
        
        tarefa.save()
        return JsonResponse({
            'status': 'ok',
            'tarefa': {
                'id': tarefa.id,
                'titulo': tarefa.titulo,
                'descricao': tarefa.descricao,
                'concluida': tarefa.concluida
            }
        })


# Toggle conclusão da tarefa
@csrf_exempt
def toggle_tarefa(request, id):
    if request.method == 'POST':
        tarefa = get_object_or_404(Tarefa, id=id)
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
        return JsonResponse({
            'status': 'ok',
            'concluida': tarefa.concluida
        })


# DELETAR (DELETE) - Excluir tarefa
@csrf_exempt
def delete_tarefa(request, id):
    if request.method == 'DELETE' or request.method == 'POST':
        tarefa = get_object_or_404(Tarefa, id=id)
        tarefa.delete()
        return JsonResponse({'status': 'ok'})
