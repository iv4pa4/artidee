from testing.gpt import chat_with_gpt
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json
import requests
import os

from app import app
from app import base
from app import db
from app import auth_url

from firebase_admin import auth

mood = 3
abstraction = 2
additional = ""
if additional:
    additional = "And " + additional

moods = ("awful",
         "bad",
         "in the middle",
         "good", 
         "awesome")

abstractions = ("specific",
                "somewhat specific",
                "vague")

print("Please tell me what to draw. My mood today is " + moods[mood] + ". Also, " + abstractions[abstraction] + additional + ". Be very brief - a few words or a sentence at most.")

def prompt(mood, abstraction, additional, user_id):
    response = chat_with_gpt("Please tell me what to draw. My mood today: " + moods[mood] + ". How specific is the drawing theme: , " + abstractions[abstraction] + ". Make it just a short sentence!")
            
    blacklist_ref = db.collection("Blacklist").document(user_id)
    blacklist_data = blacklist_ref.get()
    if blacklist_data.exists and len(blacklist_data.to_dict().get("topics", [])) > 0:
        blacklist = blacklist_data.to_dict().get("topics", [])
        if len(blacklist) > 0 and response in blacklist:
            return prompt(mood, abstraction, additional, user_id)
    
    blacklist_ref.update({"topics": firestore.ArrayUnion([response]), "user_id": user_id})
    # blacklist_ref.set({"user_id": })

    return response


# print(prompt(mood, abstraction, additional, user_id))