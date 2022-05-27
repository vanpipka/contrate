from django import forms
from .models import CargoType, TransportUnit


class CargoTypeForm(forms.ModelForm):

    class Meta:
        model = CargoType
        fields = ('name', 'iso',)


class TransportUnitForm(forms.ModelForm):

    class Meta:
        model = TransportUnit
        fields = ('name', 'cargoType',)
