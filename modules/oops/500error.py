from django.shortcuts import render
from django.http import HttpResponse
from modules.css.choose import getTheme
from modules.css.iconset import mark_icon

def response_500(request, exception):
    data = {"name": "test"}
    return render(
        request,
        'oops/500.html',
        {
            "notice_icon": mark_icon,
            "stylesheet": getTheme()
        }
    )