from app import app
from app import base

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

    return jsonify({"msg": "User created successfully"}), 200

@app.route('/login', methods=['POST'])
def log_in() -> UserRecord:
    json_data = request.json
    email = json_data.get('email')
    password = 