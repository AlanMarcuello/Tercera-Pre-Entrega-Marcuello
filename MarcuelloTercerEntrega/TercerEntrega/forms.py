from django import forms

class MallasFormulario(forms.Form):
    nombreModelo = forms.CharField(max_length=40)
    info = forms.CharField(max_length=40)
    talles = forms.CharField(max_length=40)
    colores = forms.CharField(max_length=40)

class RopaInteriorFormulario(forms.Form):
    nombreModelo = forms.CharField(max_length=40)
    info = forms.CharField(max_length=40)
    talles = forms.CharField(max_length=40)
    colores = forms.CharField(max_length=40)

class PijamasFormulario(forms.Form):
    nombreModelo = forms.CharField(max_length=40)
    inviernoverano= forms.CharField(max_length=40)
    talles = forms.CharField(max_length=40)
    colores = forms.CharField(max_length=40)