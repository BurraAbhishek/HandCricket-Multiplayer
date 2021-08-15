from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from modules.signup.forms import SignupForm

def sign_up(request):
    form = SignupForm()
    return render(request, 'templates/register.html', {"form": form})
