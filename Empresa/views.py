from rest_framework import viewsets
from Empresa.models import Funcionario, Cargo
from Empresa.serializer import FuncionarioSerializer, CargoSerializer

class FuncionariosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os Funcionarios e alunas"""
  queryset = Funcionario.objects.all()
  serializer_class = FuncionarioSerializer

class CargosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os Cargos"""
  queryset = Cargo.objects.all()
  serializer_class = CargoSerializer
