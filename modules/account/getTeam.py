from bin.mongodb.controllers import mongo_client
from modules.team_models import Anonymous, Computer

def getTeam(teamname):
    if teamname == "Anonymous":
        team_data_json = Anonymous.Anonymous
    elif teamname == "Computer":
        team_data_json = Computer.Anonymous
    else:
        user_team_name = teamname
        database = mongo_client.getConnection()
        accounts = database.get_collection("accounts")
        param = dict(_id=user_team_name)
        team_data_json = accounts.find_one(param)
    return team_data_json

