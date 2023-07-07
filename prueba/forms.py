from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Plantas, Tierras, Macetas


class CustomUserCreationForm(UserCreationForm):

    #validacion de usuario ya existente
    def username_correcto(self):
        username = self.cleaned_data["username"].lower()
        new = User.objects.filter(username = username)

        if new.count():
            raise ValidationError("Usuario ya existente")


    #validacion de email ya existente
    def email_correcto(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("email ya existente")
        return email


    #validaciones de contraseñas correctas
    def correcto_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("No son iguales, repita por favor!")
        return password2

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class PlantasForm(forms.ModelForm):
    
    class Meta:
        model = Plantas
        fields = '__all__'

class MacetasForm(forms.ModelForm):

    class Meta:
        model = Macetas
        fields = '__all__'

class TierrasForm(forms.ModelForm):

    class Meta:
        model = Tierras
        fields = '__all__'