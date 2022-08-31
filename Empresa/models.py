from django.db import models

class Funcionario(models.Model):
  nome = models.CharField(max_length=30)
  rg = models.CharField(max_length=9)
  cpf = models.CharField(max_length=11)
  data_nascimento = models.DateField()

  def __str__(self):
    return self.nome 

class Cargo(models.Model):
  Nivel = (
    ("E", "Estagiário" ),
    ("A", "Analista"),
    ("G", "Gerente")
  )

  codigo_Cargo = models.CharField(max_length=10)
  descricao = models.CharField(max_length=100)
  nivel = models.CharField(max_length=1, choices=Nivel, blank=False, null=False, default="E")

  def __str__(self):
    return self.descricao
