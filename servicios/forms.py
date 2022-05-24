from pyexpat import model
from django.forms import DateInput, DateTimeInput
from django import forms

from .models import agendamiento_citas, carton_vacuna, hospitalizacion,  receta_medica

class FormularioCitas(forms.ModelForm):
    class Meta:
        model = agendamiento_citas
        fields = '__all__'
        widgets = {'fecha_cita': DateInput(attrs={'type':'date'})}


class FormularioCarVa(forms.ModelForm):
    class Meta:
        model = carton_vacuna
        fields = '__all__'
        widgets = {'fecha_vacuna': DateInput(attrs={'type':'date'})}


class FormularioHospi(forms.ModelForm):
    class Meta:
        model = hospitalizacion
        fields = '__all__'
        widgets = {'ingreso': DateTimeInput(attrs={'type':'datetime'}),
        'egreso':DateInput(attrs={'type':'date'})}


class FormularioReceta(forms.ModelForm):
    class Meta:
        model = receta_medica
        fields = '__all__'
        
