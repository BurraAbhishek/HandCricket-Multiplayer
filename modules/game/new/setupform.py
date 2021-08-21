from django import forms

class GameSetup(forms.Form):
    gametype = forms.ChoiceField(
        choices=[(False, 'Limited-overs cricket'), (True, 'Test Cricket')], 
        label="Game Format",
        widget=forms.Select(attrs={'onchange': "toggleFormat();"})
        )
    wickets = forms.IntegerField(min_value=1, max_value=10, initial=10)
    overs = forms.IntegerField(min_value=1, initial=20, required=False)
    days = forms.IntegerField(min_value=1, initial=5, label="Maximum duration of Test match (in days)", required=False)
