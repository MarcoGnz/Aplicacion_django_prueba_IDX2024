from django import forms
from .models import Ejemplo

class EjemploForm(forms.ModelForm):
    class Meta:
        model = Ejemplo
        fields = ['nombre', 'descripcion']