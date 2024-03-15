from app import app, db
from flask import request, jsonify
from app.drawing_prompt import drawing_prompt
from app.openai_api_functions import image_generator

@app.route('/prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    mood = data.get('mood')
    abstraction = 0
    additional = data.get('additional')
    user_id = data.get('user_id')

    query = db.collection('Blacklist').where('user_id', '==', user_id)
    docs = query.stream()

    for doc in docs:
        abstraction = doc.get('level')

    if mood < 0 or mood > 4 or abstraction < 0 or abstraction > 2 or not user_id:
        return jsonify({'error': 'Missing parameters'}), 400

    generated_prompt = drawing_prompt(mood, abstraction, additional, user_id)

    if abstraction == 0:
        generated_image = image_generator(generated_prompt + ", slightly realistic drawing art style")
        return jsonify({'prompt': generated_prompt, 'image_url': generated_image})

    return jsonify({'prompt': generated_prompt})
