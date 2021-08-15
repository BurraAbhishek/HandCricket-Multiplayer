from django.shortcuts import render
from django.http import HttpResponseRedirect
from modules.css.iconset import settings_icon, mark_icon
from modules.css import choose
from django import forms
from django.forms.widgets import PasswordInput
from bin.mongodb.controllers import mongo_client
from django.contrib.auth.hashers import check_password

class CloseAccountForm(forms.Form):
    password = forms.CharField(widget=PasswordInput)


def profile_view(request):
    if 'team' in request.session:
        signin = request.session['team']
        signin_action = "/profile/"
        form = CloseAccountForm()
        return render(
            request, 
            'templates/closeaccount.html', 
            {
                "appbar": 'templates/appbar.html',
                "stylesheet": choose.getTheme(),
                "form": form,
                "settingsicon": settings_icon,
                "warningicon": mark_icon,
                "signin": signin,
                "signin_action": signin_action
            }
        )
    else:
        return HttpResponseRedirect('/login/')


def close(request):
    if request.method == "POST":
        form = CloseAccountForm(request.POST)
        if form.is_valid():
            try:
                user_team_name = request.session['team']
                user_password = form.cleaned_data['password']
                database = mongo_client.getConnection()
                if not mongo_client.ifCollectionExists(database, "accounts"):
                    database.create_collection("accounts")
                accounts = database.get_collection("accounts")
                param = dict(_id=user_team_name)
                team_data_json = accounts.find_one(param)
                if check_password(user_password, team_data_json['team_key']):
                    # Close the team account
                    accounts.update_one({"_id": request.session['team']}, { "$set": {"online": False}})
                    accounts.update_one({"_id": request.session['team']}, { "$set": {"disabled": True}})
                    del request.session['team']
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/login/')
            except:
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        signin = "Sign In"
        signin_action = "/login/"
        if 'team' in request.session:
            signin = request.session['team']
            signin_action = "/profile/"
        return render(
        request, 
        'templates/lobby.html', 
        {
            "appbar": 'templates/appbar.html',
            "stylesheet": choose.getTheme(),
            "settingsicon": settings_icon,
            "signin": signin,
            "signin_action": signin_action
        }
    )