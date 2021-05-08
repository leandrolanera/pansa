from django.urls import path
from .views import home, lista_projetos, detalhe_projeto

urlpatterns = [
    path('', home, name='home'),
    path('projetos', lista_projetos, name='lista-projetos'),
    path('detalhes/<int:id>/', detalhe_projeto, name='detalhe_projeto'),
]