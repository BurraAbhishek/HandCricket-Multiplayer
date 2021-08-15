from django.shortcuts import render
from django.http import HttpResponseRedirect
from modules.css.iconset import settings_icon
from modules.css import choose

def profile_view(request):
    if 'team' in request.session:
        signin = request.session['team']
        signin_action = "/profile/"
        return render(
            request, 
            'templates/profile.html', 
            {
                "appbar": 'templates/appbar.html',
                "stylesheet": choose.getTheme(),
                "settingsicon": settings_icon,
                "signin": signin,
                "signin_action": signin_action
            }
        )
    else:
        return HttpResponseRedirect('/login/')