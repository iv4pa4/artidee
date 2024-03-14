from gpt import chat_with_gpt
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(os.path.join(os.getcwd(), "app\\kocosi-firebase-key.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()

mood = 3
abstraction = 2
additional = ""
if additional:
    additional = "And " + additional

moods = ("very bad",
         "bad",
         "in the middle",
         "good", 
         "very good")

abstractions = ("tell me exactly what to draw, nothing abstract.",
                "give me the main idea on what to draw but be slightly abstract.",
                "today I feel creative, please give me a very abstract idea to draw.")

print("Please tell me what to draw. My mood today is " + moods[mood] + ". Also, " + abstractions[abstraction] + additional + ". Be very brief - a few words or a sentence at most.")
def prompt(mood, abstraction, additional, user_id):
    response = chat_with_gpt("Please tell me what to draw. My mood today is " + moods[mood] + ". Also, " + abstractions[abstraction] + additional + ". Be very brief - a few words or a sentence at most.")

    if response in blacklist:
        prompt(mood, abstraction, additional)
            
    blacklist_ref = db.collection("Blacklist").document(user_id)
    blacklist_data = blacklist_ref.get()
    if blacklist_data.exists:
        blacklist = blacklist_data.to_dict().get("prompts", [])
        if response in blacklist:
            return prompt(mood, abstraction, additional, user_id)
    
    blacklist_ref.update({"prompts": firestore.ArrayUnion([response])})

    return response


# print(prompt(mood, abstraction, additional, user_id))