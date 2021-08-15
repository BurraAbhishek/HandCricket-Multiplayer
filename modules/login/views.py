from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from modules.login.forms import LoginForm
from modules.css import choose
from modules.css.iconset import settings_icon, mark_icon
from bin.mongodb.controllers import mongo_client

def form_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user_team_name = form.cleaned_data['team_name']
                user_password = form.cleaned_data['password']
                database = mongo_client.getConnection()
                if not mongo_client.ifCollectionExists(database, "accounts"):
                    database.create_collection("accounts")
                accounts = database.get_collection("accounts")
                param = dict(_id=user_team_name)
                team_data_json = accounts.find_one(param)
                if check_password(user_password, team_data_json['team_key']):
                    if team_data_json['disabled']:
                        # This team is closed.
                        if team_data_json['tosViolation']:
                            text = "Your team was closed by the moderators. "
                            # Closed by moderators
                            return render(
                                request, 
                                'templates/closed.html', 
                                {
                                    "appbar": 'templates/appbar.html',
                                    "form": None,
                                    "info": text,
                                    "settingsicon": settings_icon,
                                    "signin": "Sign In",
                                    "onsubmit": "displaynone",
                                    "warningicon": mark_icon,
                                    "stylesheet": choose.getTheme()
                                }
                            )
                        else:
                            # Closed by team
                            text = "If you closed your team, but have since "
                            text += "changed your mind, you get one chance "
                            text += "of getting your team back.\n\n"
                            text += "This will work only once\n\n"
                            text += "If you close your team a second time, "
                            text += "there will be no way of recovering it."
                            text += "\n\nTo recover your team, "
                            text += "enter your team name and password "
                            text += "in the form below and click on "
                            text += "'REOPEN TEAM'."
                            return render(
                                request, 
                                'templates/closed.html', 
                                {
                                    "appbar": 'templates/appbar.html',
                                    "form": form,
                                    "info": text,
                                    "settingsicon": settings_icon,
                                    "signin": "Sign In",
                                    "onsubmit": "displayblock",
                                    "warningicon": mark_icon,
                                    "stylesheet": choose.getTheme()
                                }
                            )
                    else:
                        # Login
                        accounts.update_one({"_id": user_team_name}, { "$set": {"online": True}})
                        request.session['team'] = form.cleaned_data['team_name']
                        return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/login/')
            except:
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        form = LoginForm()
        return render(request, 'templates/login.html', {"form": form, "stylesheet": choose.getTheme()})