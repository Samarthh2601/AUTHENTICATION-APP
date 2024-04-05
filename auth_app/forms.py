from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import EUser

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=500)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=10)
    
    class Meta:
        model = EUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'zip_code']