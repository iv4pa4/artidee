from openai import OpenAI
from key import my_key

client = OpenAI(
    api_key=my_key,
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo"
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input = input("type:")
        if user_input == "quit":
            break

        try:
            response = chat_with_gpt(user_input)
            print("reply:", response)
        except Exception as e:
            print("An error occurred:", e)