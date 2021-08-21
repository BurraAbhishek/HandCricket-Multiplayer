from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from modules.signup.models import reservedWords, canBeUsed
from modules.signup.forms import SignupForm
from modules.css import choose
from modules.game.new.generate_gameid import returnGameId
from bin.mongodb.controllers import mongo_client
import math

def generate_game(team1, team2, isTest, overs, wickets, days):
    followon = 0
    if isTest:
        overs = math.inf
        if days == 1:
            followon = 75
        elif days == 2:
            followon = 100
        elif days == 3 or days == 4:
            followon = 150
        elif days > 4:
            followon = 200
    else:
        days = 0
    game_data_json = {
        "_id": returnGameId(),
        "team1": team1['team_name'],
        "team2": team2['team_name'],
        "isTest": isTest,
        "overs": overs,
        "wickets": wickets,
        "followon": followon,
        "toss": None,
        "toss_decision": None,
        "completed": False,
        "innings": [],
        "margin": "Game is yet to start.",
        "winner": None,
    }
    database = mongo_client.getConnection()
    if not mongo_client.ifCollectionExists(database, "games"):
        database.create_collection("games")
    games = database.get_collection("games")
    games.insert_one(game_data_json)
    return game_data_json
