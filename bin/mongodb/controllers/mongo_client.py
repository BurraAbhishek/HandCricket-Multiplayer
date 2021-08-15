import pymongo


def getConnection():
    # Name of the database
    databaseName = "lipyhandcricket"

    # Server address. Default is localhost:27017
    serveraddr = "mongodb://localhost:27017"

    # Client
    client = pymongo.MongoClient(serveraddr)

    # Database
    database = client[databaseName]

    return database


def ifCollectionExists(database, collection):
    result = False
    collection_list = database.list_collection_names()
    if collection in collection_list:
        result = True
    return result

