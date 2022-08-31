from django.contrib import admin
from django.urls import path, include
from Empresa.views import FuncionariosViewSet, CargosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Funcionarios', FuncionariosViewSet, basename='Funcionarios')
router.register('Cargos', CargosViewSet, basename='Cargos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
