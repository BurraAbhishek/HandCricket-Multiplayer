from django import forms
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    team_name = forms.CharField(label='Team name', max_length=100)
    password = forms.CharField(widget=PasswordInput)