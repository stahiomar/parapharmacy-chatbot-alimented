from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'First Name...',
    'class': 'form-control'
  }) )
  last_name = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Last Name...',
    'class': 'form-control'
  }) )
  email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Email...',
    'class': 'form-control'
  }) )
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Password...',
    'class': 'form-control'
  }) )
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password...',
    'class': 'form-control'
  }) )

  class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

