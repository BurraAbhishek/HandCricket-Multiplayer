from django.shortcuts import render
from modules.css.iconset import settings_icon
from modules.css import choose

def lobby_view(request):
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