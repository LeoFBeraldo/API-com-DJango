from dataclasses import fields
from rest_framework import serializers
from Empresa.models import Funcionario, Cargo

class FuncionarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Funcionario
    fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CargoSerializer (serializers.ModelSerializer):
  class Meta:
    model = Cargo
    fields = '__all__'