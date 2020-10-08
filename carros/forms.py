from django import forms
from carros.models import Carro


class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ('modelo', 'fabricante', 'cor', 'ano', 'Km')
