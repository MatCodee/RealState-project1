from django import forms 
from .models import Region,City

TYPE_STATUS = [
    ("Arriendo","Arriendo"),
    ("Venta","Venta"),
]

class FormFilterSelect(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(),widget=forms.Select(
        attrs={'class': 'form-control'}
    ))
    city = forms.ModelChoiceField(queryset=City.objects.none(),widget=forms.Select(
        attrs={'class': 'form-control'}
    ))
    status = forms.ChoiceField(choices=TYPE_STATUS,required = True,widget=forms.Select(
        attrs={'class': 'form-control'}
    ))





