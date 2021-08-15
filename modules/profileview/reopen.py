from django.shortcuts import render
from django.http import HttpResponseRedirect
from modules.css.iconset import settings_icon, mark_icon
from modules.css import choose
from django import forms
from django.forms.widgets import PasswordInput
from bin.mongodb.controllers import mongo_client
from django.contrib.auth.hashers import check_password
from modules.login.forms import LoginForm


def open(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user_team_name = form.cleaned_data['team_name']
                print(user_team_name)
                user_password = form.cleaned_data['password']
                database = mongo_client.getConnection()
                if not mongo_client.ifCollectionExists(database, "accounts"):
                    database.create_collection("accounts")
                accounts = database.get_collection("accounts")
                param = dict(_id=user_team_name)
                team_data_json = accounts.find_one(param)
                if check_password(user_password, team_data_json['team_key']):
                    # Reopen the team account
                    accounts.update_one({"_id": user_team_name}, { "$set": {"disabled": False}})
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