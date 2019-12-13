from django.db import models
from django.utils import timezone



    
class Pedido(models.Model):
    metodo_pagamento = [
        ('AV', 'Pagamento à vista'),
        ('P2', 'Parcelado em 2x'),
        ('P3', 'Parcelado em 3x'),
    ]
    email = models.EmailField()
    senha = models.CharField(max_length=10)
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.senha
