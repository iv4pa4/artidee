import json
import requests
import os

from app import app
from app import base
from app import auth_url

from flask import request, jsonify

from firebase_admin import auth
from firebase_admin.auth import UserRecord

@app.route('/signup', methods=['POST'])
def sign_up() -> UserRecord:
    json_data = request.json
    email = json_data.get('email')
    password = json_data.get('password')

    try:
        auth.create_user(email=email, password=password)
    except ValueError as ve:
        # Handle ValueError (raised when email or password is invalid)
        return jsonify({"msg": str(ve)}), 400
    except Exception as e:
        # Catch any other unexpected errors
        return jsonify({"msg": str(e)}), 500

    return jsonify({"message": auth.get_user_by_email(email).uid}), 200

@app.route('/login', methods=['POST'])
def log_in() -> UserRecord:
    json_data = request.json
    email = json_data.get('email')
    password = json_data.get('password')

    key = open(os.path.join(os.getcwd(), "app\\web_api_key.txt"), 'r')
    response = requests.post(auth_url,
                    params={"key": key.read()},
                    data=request.json)

    if response.status_code >= 300:
        return response.text, response.status_code
    else:
        print('upload image')
        return jsonify({"message": auth.get_user_by_email(email).uid}), response.status_code