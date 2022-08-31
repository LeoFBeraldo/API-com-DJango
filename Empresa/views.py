from rest_framework import viewsets
from Empresa.models import Funcionario, Cargo, Matricula
from Empresa.serializer import FuncionarioSerializer, CargoSerializer, MatriculaSerializer

class FuncionariosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os Funcionarios e alunas"""
  queryset = Funcionario.objects.all()
  serializer_class = FuncionarioSerializer

class CargosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os Cargos"""
  queryset = Cargo.objects.all()
  serializer_class = CargoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
  """Indentificando Matriculas"""
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer
