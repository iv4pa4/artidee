from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from testing.generate_prompt import prompt

cred = credentials.Certificate(os.path.join(os.getcwd(), "app\\kocosi-firebase-key.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route('/prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    mood = data.get('mood')
    abstraction = data.get('abstraction')
    additional = data.get('additional')
    user_id = data.get('user_id')

    if not all([mood, abstraction, additional, user_id]):
        return jsonify({'error': 'Missing parameters'}), 400
    
    generated_prompt = prompt(mood, abstraction, additional, user_id)
    
    return jsonify({'prompt': generated_prompt})

@app.route('/prompts/<user_id>', methods=['GET'])
def get_prompts(user_id):
    blacklist_ref = db.collection("Blacklist").document(user_id)
    blacklist_data = blacklist_ref.get()
    if not blacklist_data.exists:
        return jsonify({'error': 'User has no prompts'}), 404
    
    prompts = blacklist_data.to_dict().get("prompts", [])
    
    return jsonify({'prompts': prompts})
