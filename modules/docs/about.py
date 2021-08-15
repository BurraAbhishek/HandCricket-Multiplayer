from django.shortcuts import render
from modules.css import choose
from modules.css.iconset import settings_icon

def open(request):
    signin = "Sign In"
    signin_action = "/login/"
    if 'team' in request.session:
        signin = request.session['team']
        signin_action = "/profile/"
    return render(
        request, 
        'templates/about.html', 
        {
            "appbar": 'templates/appbar.html',
            "settingsicon": settings_icon,
            "signin": signin,
            "signin_action": signin_action,
            "stylesheet": choose.getTheme()
        }
    )