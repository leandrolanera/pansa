from django.urls import path
from .views import home, lista_projetos, detalhe_projeto, lista_baseline, lista_versoes

urlpatterns = [
    path('home', home, name='home'),
    path('projetos', lista_projetos, name='lista_projetos'),
    path('versoes', lista_versoes, name='lista_versoes'),
    path('detalhes/<int:id>/', detalhe_projeto, name='detalhe_projeto'),
    path('baseline/<str:nomeVersao>/', lista_baseline, name='lista_baseline'),    
]