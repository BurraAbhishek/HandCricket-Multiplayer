from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from modules.signup.forms import EditprofileForm
from modules.profileview.closeaccount import CloseAccountForm
from modules.css import choose
from modules.css.iconset import settings_icon
from bin.mongodb.controllers import mongo_client

def form_view(request):
    if request.method == "POST":
        postform = CloseAccountForm(request.POST)
        if postform.is_valid():
            try:
                user_team_name = request.session['team']
                database = mongo_client.getConnection()
                if not mongo_client.ifCollectionExists(database, "accounts"):
                    database.create_collection("accounts")
                accounts = database.get_collection("accounts")
                param = dict(_id=user_team_name)
                team_data_json = accounts.find_one(param)
                if(team_data_json['isHuman']):
                    isHuman = "Human"
                else:
                    isHuman = "Bot"
                form = EditprofileForm({
                    "team_name": request.session['team'],
                    "member1": team_data_json['team_members'][0],
                    "member2": team_data_json['team_members'][1],
                    "member3": team_data_json['team_members'][2],
                    "member4": team_data_json['team_members'][3],
                    "member5": team_data_json['team_members'][4],
                    "member6": team_data_json['team_members'][5],
                    "member7": team_data_json['team_members'][6],
                    "member8": team_data_json['team_members'][7],
                    "member9": team_data_json['team_members'][8],
                    "member10": team_data_json['team_members'][9],
                    "member11": team_data_json['team_members'][10],
                    "password": postform.cleaned_data['password'],
                    "Account_type": isHuman
                })
                signin = request.session['team']
                signin_action = "/profile/"
                return render(
                    request, 
                    'templates/editteam.html', 
                    {
                        "appbar": 'templates/appbar.html',
                        "form": form,
                        "stylesheet": choose.getTheme(),
                        "settingsicon": settings_icon,
                        "signin": signin,
                        "signin_action": signin_action
                    }
                )
            except:
                return HttpResponseRedirect('/login/')


def update(request):
    if request.method == "POST":
        form = EditprofileForm(request.POST)
        if form.is_valid():
            team_data_json = {
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
                        "team_key": make_password(form.cleaned_data['password']),
                    }
            database = mongo_client.getConnection()
            if not mongo_client.ifCollectionExists(database, "accounts"):
                database.create_collection("accounts")
            accounts = database.get_collection("accounts")
            accounts.update_one({"_id": request.session['team']}, { "$set": {"team_members": team_data_json["team_members"]}})
            accounts.update_one({"_id": request.session['team']}, { "$set": {"team_key": team_data_json["team_key"]}})
            return HttpResponseRedirect('/')
