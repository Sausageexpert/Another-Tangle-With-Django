from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm): # to have a class inheriting from UserCreationForm
    email = forms.EmailField()
    class Meta(): # meta is data about data, in this case about the registerform class
        model=User
        fields=['username', 'email', 'password1', 'password2']
        
