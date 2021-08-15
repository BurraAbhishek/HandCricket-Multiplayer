from django.db import models

# Create your models here.
reservedWords = [
    "test",
    "anonymous",
    "guest",
    "computer",
    "moderator",
    "cpu"
]

def canBeUsed(name, bannedList) -> bool:
    response = True
    for i in bannedList:
        if i.lower() == name.lower():
            response = False
            break
    return response
