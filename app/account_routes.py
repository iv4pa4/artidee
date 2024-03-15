import requests
import os

from app import app, base, auth_url, db

from flask import request, jsonify

from firebase_admin import auth
from firebase_admin.auth import UserRecord

@app.route('/signup', methods=['POST'])
def sign_up() -> UserRecord:
    try:
        auth.create_user(email=request.json['email'], password=request.json['password'], display_name=request.json['name'])
        update_time, doc_id = db.collection("Blacklist").add({"level": request.json['level'], "topic": [""], "user_id": auth.get_user_by_email(request.json['email']).uid})
    except ValueError as ve:
        # Handle ValueError (raised when email or password is invalid)
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        # Catch any other unexpected errors
        return jsonify({"message": str(e)}), 500

    return jsonify({"message": auth.get_user_by_email(request.json['email']).uid}), 200

@app.route('/login', methods=['POST'])
def log_in() -> UserRecord:
    key = open(os.path.join(os.getcwd(), "keys\\web_api_key.txt"), 'r')
    response = requests.post(auth_url,
                    params={"key": key.read()},
                    data=request.json)

    if response.status_code >= 300:
        return response.text, response.status_code
    else:
        return jsonify({"message": auth.get_user_by_email(request.json['email']).uid}), response.status_code