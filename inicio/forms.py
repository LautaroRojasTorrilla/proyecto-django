from django import forms

class CracionAnimalFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class BuscarAnimal(forms.Form):
    # permite que el campo este vacío
    nombre = forms.CharField(max_length=20, required=False)