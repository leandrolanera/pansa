from django.urls import path
from .views import home, lista_projetos

urlpatterns = [
    path('', home, name='home'),
    path('projetos', lista_projetos, name='lista-projetos'),
]