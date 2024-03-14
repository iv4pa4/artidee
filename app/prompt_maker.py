from openai import OpenAI

with open('key.txt', 'r') as file:
    my_key = file.read()

client = OpenAI(
    api_key=my_key,
)

def prompt_maker(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        temperature=1.5
    )
    return response.choices[0].message.content