from gpt import chat_with_gpt
from blacklist import blacklist

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
def prompt(mood, abstraction, additional):
    response = chat_with_gpt("Please tell me what to draw. My mood today is " + moods[mood] + ". Also, " + abstractions[abstraction] + additional + ". Be very brief - a few words or a sentence at most.")

    if response in blacklist:
        prompt(mood, abstraction, additional)
            
    blacklist.append(response)

    return response


print(prompt(mood, abstraction, additional))