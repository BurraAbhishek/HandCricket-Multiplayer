import datetime


def applyTheme(theme):
    themes_map = {
            "Light": "templates/light.html",
            "Dark": "templates/dark.html"
        }
    try:
        return themes_map[theme]
    except:
        return themes_map[getThemeByTime()]


def getThemeByTime():
    d = datetime.datetime.now()
    h = d.hour
    if h >= 6 and h < 18:
        theme = "Light"
    else:
        theme = "Dark"
    return theme


def getTheme():
    return applyTheme(getThemeByTime())