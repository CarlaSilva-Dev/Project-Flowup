# tasks/models.py

from django.db import models

STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('completo', 'Completo'),
]

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    descricao = models.TextField(blank=True, null=True) 
    
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pendente'
    )
    
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo