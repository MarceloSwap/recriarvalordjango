from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class CriarContaForm(UserCreationForm):
    # obriga o django a pedir o email na criação da conta
    email = forms.EmailField()

    class Meta:
        model = Usuario
        # nome padrão do campo coloque sua senha = password1, e para senha password2
        fields = ('username', 'email', 'password1', 'password2')

# forms.Form é o formulario padrão do django
class HomeForm(forms.Form):
    email = forms.EmailField(label=False)