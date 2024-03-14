from openai import OpenAI
import random

with open('key.txt', 'r') as file:
    my_key = file.read()

client = OpenAI(
    api_key=my_key,
)

def chat_with_gpt(prompt):
    # tempr = random.random() * 2
    # print(tempr)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        temperature=1.99
    )
    return response.choices[0].message.content

# if __name__ == "__main__":
#     while True:
#         user_input = input("type:")
#         if user_input == "quit":
#             break

#         try:
#             response = chat_with_gpt(user_input)
#             print("reply:", response)
#         except Exception as e:
#             print("An error occurred:", e)
