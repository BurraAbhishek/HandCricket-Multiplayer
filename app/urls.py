"""HandCricket_Multiplayer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from modules.signup import views as signup_views
from modules.lobby import views as lobby_views
from modules.login import views as login_views
from modules.login import logout as logout_user
from modules.profileview import views as profile_views
from modules.profileview import closeaccount, reopen, edit
from modules.docs import about, license

urlpatterns = [
    path('', lobby_views.lobby_view, name='lobby_view'),
    # Account related
    path('signup/', signup_views.form_view, name='form_view'),
    path('login/', login_views.form_view, name='form_view'),
    path('logout/', logout_user.logout, name='logout'),
    path('account/close/', closeaccount.profile_view, name='profile_view'),
    path('account/closepermanently/', closeaccount.close, name='close'),
    path('account/reopen/', reopen.open, name='open'),
    path('profile/', profile_views.profile_view, name='profile_view'),
    path('editteam/edit/', edit.form_view, name="form_view"),
    path('editteam/update/', edit.update, name="update"),
    # Documentation
    path('about/', about.open, name='open'),
    path('license/', license.open, name='open'),
]
