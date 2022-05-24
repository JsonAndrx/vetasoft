from django.forms import DateInput
from django import forms

from .models import pacientes, propietario, veterinario

class FormularioPacientes(forms.ModelForm):
    class Meta:
        model = pacientes
        fields = '__all__'
        widgets = {'fecha_nacimiente': DateInput(attrs={'type':'date'})}


class FormularioPropietario(forms.ModelForm):
    class Meta:
        model = propietario
        fields = '__all__'
        

class FormularioVeterinario(forms.ModelForm):
    class Meta:
        model = veterinario
        fields = '__all__'