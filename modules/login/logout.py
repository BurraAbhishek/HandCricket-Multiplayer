from django.http import HttpResponseRedirect
from bin.mongodb.controllers import mongo_client

def logout(request):
    database = mongo_client.getConnection()
    if not mongo_client.ifCollectionExists(database, "accounts"):
        database.create_collection("accounts")
    accounts = database.get_collection("accounts")
    accounts.update_one({"_id": request.session['team']}, { "$set": {"online": False}})
    if 'team' in request.session:
        del request.session['team']
    return HttpResponseRedirect('/')
    