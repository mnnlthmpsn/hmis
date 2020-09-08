from django import forms
from .models import Staff

class LoginForm(forms.Form):
    staff_ID = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Staff ID'
            }
        ))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))