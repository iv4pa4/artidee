from app.openai_api_functions import prompt_maker
from app import db
from firebase_admin import firestore

moods = ("awful",
         "bad",
         "in the middle",
         "good", 
         "awesome")

abstractions = ("specific",
                "somewhat specific",
                "vague")

def drawing_prompt(mood, abstraction, additional, user_id):
    if additional:
        additional = "And " + additional

    response = prompt_maker("Please tell me what to draw. My mood today: " + moods[mood] + ". How specific is the drawing theme: , " + abstractions[abstraction] + additional + ". Make it just a short sentence!")
            
    blacklist_ref = db.collection("Blacklist").document(user_id)
    blacklist_data = blacklist_ref.get()

    if blacklist_data.exists:
        blacklist = blacklist_data.to_dict().get("topics", [])
        if response in blacklist:
            return drawing_prompt(mood, abstraction, additional, user_id)
    
    blacklist_ref.update({"topics": firestore.ArrayUnion([response])})

    if "user_id" not in blacklist_data.to_dict():
        blacklist_ref.update({"user_id": user_id})

    response = response.strip('/"')
    
    if response in blacklist:
        return drawing_prompt(mood, abstraction, additional, user_id)

    return response