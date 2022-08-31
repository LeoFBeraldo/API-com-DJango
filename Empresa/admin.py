from django.contrib import admin
from Empresa.models import Funcionario, Cargo, Matricula

class Funcionarios(admin.ModelAdmin):
  list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
  list_display_links = ('id', 'nome')
  search_fields = ('nome',)
  list_per_page = 20

admin.site.register(Funcionario, Funcionarios)

class Cargos(admin.ModelAdmin):
  list_display = ('id', 'codigo_Cargo', 'descricao')
  list_display_links = ('id', 'codigo_Cargo')
  search_fields = ('codigo_Cargo',)

admin.site.register(Cargo, Cargos)

class Matriculas(admin.ModelAdmin):
  list_display = ('id', 'Funcionario', 'Cargo', 'Periodo')
  list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)
