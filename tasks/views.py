# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Tarefa 
from .forms import TarefaForm 


def listar_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-criado_em')
    
    for tarefa in tarefas:
        tarefa.cor_status = "green" if tarefa.status == "completo" else "orange"
        
    contexto = {'tarefas': tarefas}
    # CAMINHO CORRIGIDO: 'tasks/lista_tarefas.html'
    return render(request, 'tasks/lista_tarefas.html', contexto) 


def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas') 
    else:
        form = TarefaForm()
    
    # CAMINHO CORRIGIDO: 'tasks/criar_tarefa.html'
    return render(request, 'tasks/criar_tarefa.html', {'form': form})


@require_http_methods(["GET", "POST"]) 
def gerenciar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    cor_status = "green" if tarefa.status == "completo" else "orange"

    if request.method == 'POST':
        if 'atualizar' in request.POST:
            form = TarefaForm(request.POST, instance=tarefa)
            if form.is_valid():
                form.save()
                return redirect('lista_tarefas')

        elif 'deletar' in request.POST:
            tarefa.delete()
            return redirect('lista_tarefas')

        elif 'alternar_status' in request.POST:
             tarefa.status = 'completo' if tarefa.status == 'pendente' else 'pendente'
             tarefa.save()
             return redirect('lista_tarefas')

    form = TarefaForm(instance=tarefa) 

    # CAMINHO CORRIGIDO: 'tasks/detalhe_tarefa.html'
    return render(request, 'tasks/detalhe_tarefa.html', {
        'tarefa': tarefa, 
        'form': form,
        'cor_status': cor_status
    })