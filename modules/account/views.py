import datetime
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from modules.css.iconset import settings_icon, mark_icon
from modules.css import choose
from modules.profileview.closeaccount import CloseAccountForm
from modules.account.getTeam import getTeam

def profile_view(request, teamname):
    if 'team' in request.session:
        signin = request.session['team']
    else:
        signin = "Sign In"
    signin_action = "/profile/"
    try:
        team_data = getTeam(teamname)
        if team_data['disabled']:
            return render(
                request, 
                'account/closed.html', 
                {
                    "appbar": 'templates/appbar.html',
                    "teamname": teamname,
                    "teamstatus": "This account is closed.",
                    "gamedata": None,
                    "stylesheet": choose.getTheme(),
                    "settingsicon": settings_icon,
                    "signin": signin,
                    "signin_action": signin_action
                }
            )
        else:
            notSameProfile = 'team' not in request.session or request.session['team'] != teamname
            if notSameProfile:
                if team_data['tosViolation']:
                    return render(
                        request, 
                        'account/marked.html', 
                        {
                            "appbar": 'templates/appbar.html',
                            "stats": "account/openprofiles.html",
                            "teamname": teamname,
                            "notice_icon": mark_icon,
                            "membersince": str(datetime.date.fromtimestamp(1600000000)),
                            "lastactive": "1 month ago",
                            "gamedata": None,
                            "stylesheet": choose.getTheme(),
                            "settingsicon": settings_icon,
                            "signin": signin,
                            "signin_action": signin_action
                        }
                    )
                else:
                    return render(
                        request, 
                        'account/good.html', 
                        {
                            "appbar": 'templates/appbar.html',
                            "stats": "account/openprofiles.html",
                            "teamname": teamname,
                            "membersince": str(datetime.date.fromtimestamp(1600000000)),
                            "lastactive": "1 month ago",
                            "gamedata": None,
                            "stylesheet": choose.getTheme(),
                            "settingsicon": settings_icon,
                            "signin": signin,
                            "signin_action": signin_action
                        }
                    )
            else:
                return render(
                        request, 
                        'account/good.html', 
                        {
                            "appbar": 'templates/appbar.html',
                            "stats": "account/openprofiles.html",
                            "teamname": teamname,
                            "membersince": str(datetime.date.fromtimestamp(1600000000)),
                            "lastactive": "1 month ago",
                            "gamedata": None,
                            "stylesheet": choose.getTheme(),
                            "settingsicon": settings_icon,
                            "signin": signin,
                            "signin_action": signin_action
                        }
                    )
    except:
        raise Http404()
