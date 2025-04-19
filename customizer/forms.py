from django import forms
from .models import CustomProduct


#for signup
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomProductForm(forms.ModelForm):
    class Meta:
        model = CustomProduct
        fields = ['product', 'artwork', 'description']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
