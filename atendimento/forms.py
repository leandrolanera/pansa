from django import forms
from .models import Projects

class ProjectsForm (forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name','parent_id']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }