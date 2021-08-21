from django import forms
from django.shortcuts import render
from modules.css import choose

class Toss1(forms.Form):
    toss = forms.IntegerField(max_value=6, min_value=1, label="Enter any integer from 1 to 6")


class Toss2(forms.Form):
    toss = forms.ChoiceField(choices=[(1, 'Odd'), (0, 'Even')], label="Is your opponent's input odd or even?")


class chooseBatField(forms.Form):
    selection = forms.ChoiceField(choices=[('bat', 'Bat'), ('field', 'Field')])


def call_toss(request):
    game_url = request.session['game']['_id']
    if request.session['team'] == request.session['game']['team1']: 
        description = "Enter an integer from 1 to 6. "
        description += "To win the toss, enter the integer in such a way that"
        description += " your opponent incorrectly guesses "
        description += "whether it is odd or even."
        return render(
            request, 
            'game/toss.html', 
            {
                "description": description,
                "toss": Toss1(),
                "game_redirect": game_url,
                "stylesheet": choose.getTheme(),
            }
        )
    elif request.session['team'] == request.session['game']['team2']:
        description = "Your opponent will enter an integer from 1 to 6. "
        description += "To win the toss, you have to correctly decide "
        description += "whether that number is odd or even."
        return render(
            request, 
            'game/toss.html', 
            {
                "description": description,
                "toss": Toss2(),
                "game_redirect": game_url,
                "stylesheet": choose.getTheme(),
            }
        )