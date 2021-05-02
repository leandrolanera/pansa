from django.shortcuts import render
from .models import Projects
from .forms import ProjectsForm


def home(request):
    return render(request, 'home.html')
    
def lista_projetos(request):
    projects = Projects.objects.all()
    return render(request, 'lista-projetos.html',{'projects':projects})