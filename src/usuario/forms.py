from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
user = get_user_model()
from django import forms
class CriarContaUsuario(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = user
        fields = ('username', 'email','password', 'password2')
