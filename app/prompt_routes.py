import json
import requests
import os

from app import app
from app import base
from app import db
from app import auth_url

from flask import request, jsonify

from firebase_admin import auth

from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from testing.generate_prompt import prompt

@app.route('/prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    mood = data.get('mood')
    abstraction = data.get('abstraction')
    additional = data.get('additional')
    user_id = data.get('user_id')
    
    if mood < 0 or abstraction < 0 or not user_id:
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
