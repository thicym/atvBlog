from django.db import models

# Create your models here.
from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_conclusao = models.DateField()

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class SobreMim(models.Model):
    biografia = models.TextField()

    def __str__(self):
        return "Sobre Mim"
