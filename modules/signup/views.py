from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from modules.signup.models import reservedWords, canBeUsed
from modules.signup.forms import SignupForm
from modules.css import choose
from bin.mongodb.controllers import mongo_client

def form_view(request) -> render:
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if canBeUsed(form.cleaned_data['member1'], reservedWords):
                try:
                    isHuman = True
                    if form.cleaned_data['Account_type'] == "Bot":
                        isHuman = False
                    team_data_json = {
                        "_id": form.cleaned_data['team_name'],
                        "team_name": form.cleaned_data['team_name'],
                        "team_members": [
                            form.cleaned_data['member1'],
                            form.cleaned_data['member2'],
                            form.cleaned_data['member3'],
                            form.cleaned_data['member4'],
                            form.cleaned_data['member5'],
                            form.cleaned_data['member6'],
                            form.cleaned_data['member7'],
                            form.cleaned_data['member8'],
                            form.cleaned_data['member9'],
                            form.cleaned_data['member10'],
                            form.cleaned_data['member11']
                        ],
                        "games_played": 0,
                        "games_won": 0,
                        "games_lost": 0,
                        "tests_tied": 0,
                        "team_key": make_password(form.cleaned_data['password']),
                        "online": True,
                        "hasSuperOver": False,
                        "disabled": False,
                        "tosViolation": False,
                        "isModerator": False,
                        "isHuman": isHuman
                    }
                    database = mongo_client.getConnection()
                    if not mongo_client.ifCollectionExists(database, "accounts"):
                        database.create_collection("accounts")
                    accounts = database.get_collection("accounts")
                    accounts.insert_one(team_data_json)
                    request.session['team'] = form.cleaned_data['team_name']
                    return HttpResponseRedirect('/profile/')
                except:
                    return HttpResponseRedirect('/signup/')
            else:
                return HttpResponseRedirect('/signup/')
        else:
            return HttpResponseRedirect('/signup/')
    else:
        form = SignupForm()
        return render(request, 'templates/register.html', {"form": form, "stylesheet": choose.getTheme()})