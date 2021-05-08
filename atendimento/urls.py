from django.urls import path
from .views import home, lista_projetos, detalhe_projeto, lista_baseline

urlpatterns = [
    path('', home, name='home'),
    path('projetos', lista_projetos, name='lista-projetos'),
    path('detalhes/<int:id>/', detalhe_projeto, name='detalhe_projeto'),
    path('baseline/<str:nomeVersao>/', lista_baseline, name='lista_baseline'),
]