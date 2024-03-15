from app.openai_api_functions import prompt_maker
from app import db
from firebase_admin import firestore

moods = ("very dark",
         "mildly dark",
         "neutral",
         "mildly happy",
         "very happy")

abstractions = ("somewhat specific",
                "somewhat vague",
                "very vague")

length = ("a sentence", "a couple of words to a sentence", "a couple of words")

cut_phrases = ("Draw a ", "Draw an ", "How about drawing ", "Draw : ", "Please draw a ", "Please draw an ")

beginner = (" Please include animals, creatures, places or objects.", "", "")

def drawing_prompt(mood, abstraction, additional, user_id):
    if additional:
        additional = "And " + additional

    response = prompt_maker("Please tell me what to draw. Give me a theme that reflects my mood today: " + moods[mood] + ". How specific is the drawing theme: " + abstractions[abstraction] + additional + ". Use B1 vocabulary at most and make it just" + length[abstraction] + "at most! I want your answer to be completely and solely just the theme itself." + beginner[abstraction])

    response = response.strip('/"')

    if response.endswith('.'):
        response = response[:-1]
    for phrase in cut_phrases:
        if response.startswith(phrase):
            response = response[len(phrase):]
            break

    response = response.lower()
    response = response.replace('\t', ' ')

    blacklist_ref = db.collection("Blacklist").document(user_id)
    blacklist_data = blacklist_ref.get()

    if blacklist_data.exists:
        blacklist = blacklist_data.to_dict().get("topics", [])
        if response in blacklist:
            return drawing_prompt(mood, abstraction, additional, user_id)

    topics_list = blacklist_data.to_dict().get("topics", [])
    if len(topics_list) == 50:
        topics_list.pop(0)
    topics_list.append(response)

    blacklist_ref.update({"topics": topics_list})

    if "user_id" not in blacklist_data.to_dict():
        blacklist_ref.update({"user_id": user_id})

    if response in blacklist:
        return drawing_prompt(mood, abstraction, additional, user_id)

    return response