from app import app
from flask import request, jsonify
from flask import request, jsonify
from app.drawing_prompt import drawing_prompt
from app.openai_api_functions import image_generator

@app.route('/prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    mood = data.get('mood')
    abstraction = data.get('abstraction')
    additional = data.get('additional')
    user_id = data.get('user_id')
    
    if mood < 0 or mood > 4 or abstraction < 0 or abstraction > 2 or not user_id:
        return jsonify({'error': 'Missing parameters'}), 400
    
    generated_prompt = drawing_prompt(mood, abstraction, additional, user_id)

    if abstraction == 0:
        generated_image = image_generator(generated_prompt)
        return jsonify({'prompt': generated_prompt, 'image_url': generated_image})
    
    return jsonify({'prompt': generated_prompt})
