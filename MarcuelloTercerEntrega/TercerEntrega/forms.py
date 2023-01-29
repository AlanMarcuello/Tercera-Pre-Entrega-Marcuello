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

# para crear el formulario de registro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']