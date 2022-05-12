from django import forms
from .models import CargoType


class CargoTypeForm(forms.ModelForm):

    class Meta:
        model = CargoType
        fields = ('name', 'iso',)
