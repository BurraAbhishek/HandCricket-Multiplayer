from django.shortcuts import render
from modules.css.iconset import settings_icon
from modules.css import choose
from modules.team_models import Anonymous, Computer
from modules.account.getTeam import getTeam
from modules.game.new import setupform, generate_game
from modules.game.toss import render_toss

def setup_ai(request):
    try:
        team1 = getTeam(request.session['team'])
    except:
        team1 = Anonymous.Anonymous
    team2 = Computer.Anonymous
    if request.method == "POST":
        form = setupform.GameSetup(request.POST)
        if form.is_valid():
            isTest = form.cleaned_data["gametype"]
            wickets = form.cleaned_data["wickets"]
            overs = form.cleaned_data["overs"]
            days = form.cleaned_data["days"]
            game = generate_game.generate_game(team1, team2, isTest, overs, wickets, days)
            request.session['game'] = game
            if not 'team' in request.session:
                request.session['team'] = team1['team_name']
            return render_toss.call_toss(request)



def initial(request):
    signin = "Sign In"
    signin_action = "/login/"
    if 'team' in request.session:
        signin = request.session['team']
        signin_action = "/profile/"
    return render(
        request, 
        'game/setup.html', 
        {
            "appbar": 'templates/appbar.html',
            "form": setupform.GameSetup(),
            "setup_location": "/setup/ai/play/",
            "stylesheet": choose.getTheme(),
            "settingsicon": settings_icon,
            "signin": signin,
            "signin_action": signin_action
        }
    )