from django import forms
from django.forms.widgets import PasswordInput

class SignupForm(forms.Form):
    team_name = forms.CharField(label='Team name', max_length=100)
    member1 = forms.CharField(label='Team Player 1', max_length=100)
    member2 = forms.CharField(label='Team Player 2', max_length=100)
    member3 = forms.CharField(label='Team Player 3', max_length=100)
    member4 = forms.CharField(label='Team Player 4', max_length=100)
    member5 = forms.CharField(label='Team Player 5', max_length=100)
    member6 = forms.CharField(label='Team Player 6', max_length=100)
    member7 = forms.CharField(label='Team Player 7', max_length=100)
    member8 = forms.CharField(label='Team Player 8', max_length=100)
    member9 = forms.CharField(label='Team Player 9', max_length=100)
    member10 = forms.CharField(label='Team Player 10', max_length=100)
    member11 = forms.CharField(label='Team Player 11', max_length=100)
    password = forms.CharField(widget=PasswordInput)
    Account_type = forms.ChoiceField(choices=[('Human', 'Human'), ('Bot', 'Bot')])


class EditProfileForm(forms.Form):
    member1 = forms.CharField(label='Team Player 1', max_length=100)
    member2 = forms.CharField(label='Team Player 2', max_length=100)
    member3 = forms.CharField(label='Team Player 3', max_length=100)
    member4 = forms.CharField(label='Team Player 4', max_length=100)
    member5 = forms.CharField(label='Team Player 5', max_length=100)
    member6 = forms.CharField(label='Team Player 6', max_length=100)
    member7 = forms.CharField(label='Team Player 7', max_length=100)
    member8 = forms.CharField(label='Team Player 8', max_length=100)
    member9 = forms.CharField(label='Team Player 9', max_length=100)
    member10 = forms.CharField(label='Team Player 10', max_length=100)
    member11 = forms.CharField(label='Team Player 11', max_length=100)
    password = forms.CharField(widget=PasswordInput) 
