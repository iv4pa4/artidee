from openai import OpenAI
import os

with open(os.path.join(os.getcwd(), 'keys\\key.txt'), 'r') as file:
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

def image_generator(prompt):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="512x512",
        quality="standard",
        n=1,
    )

    return response.data[0].url