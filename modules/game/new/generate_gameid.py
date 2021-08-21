import random
import string
from bin.mongodb.controllers import mongo_client


def generateFilename(size):
    game_data_savename = ''.join([random.choice(string.ascii_uppercase
        + string.ascii_lowercase + string.digits) for n in range(size)])
    return game_data_savename


def returnGameId():
    # The game URL can be anywhere between 8 and 16 characters long
    database = mongo_client.getConnection()
    if not mongo_client.ifCollectionExists(database, "games"):
        database.create_collection("games")
    games = database.get_collection("games")
    gameid = generateFilename(random.randint(8, 16))
    while games.count_documents({ "_id": gameid}, limit = 1):
        gameid = generateFilename(random.randint(8, 16))
    return gameid