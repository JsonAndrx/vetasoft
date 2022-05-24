from django import forms
from django.forms import DateInput

from .models import vacunas, medicina, inventario

class FormularioVacunas(forms.ModelForm):
    class Meta:
        model = vacunas
        fields = '__all__'


class FormularioMedicina(forms.ModelForm):
    class Meta:
        model = medicina
        fields = '__all__'


class FormularioInventario(forms.ModelForm):
    class Meta:
        model = inventario
        fields = '__all__'
        widgets = {'inventario_fecha':DateInput(attrs={'type':'date'})}