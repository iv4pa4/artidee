from gpt import chat_with_gpt
from blacklist import blacklist

mood = 4
abstraction = 0
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
                "today I feel creative, please give me quite an abstract idea to draw.")

print("Please tell me what to draw. My mood today is " + moods[mood] + ". Also, " + abstractions[abstraction] + additional + ". Be very brief - a few words or a sentence at most.")
def prompt(mood, abstraction, additional):
    response = chat_with_gpt("Please tell me what to draw. My mood today is " + moods[mood] + ". Also, " + abstractions[abstraction] + additional + ". Be very brief - a few words or a sentence at most.")

    for sentence in blacklist:
        if response == sentence:
            prompt(mood, abstraction, additional)
            
    blacklist.append(response)

    return response


print(prompt(mood, abstraction, additional))