from django.db import models

class Livros(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('descricao',max_length=100)
    autor = models.CharField('autor',max_length=100)
 

