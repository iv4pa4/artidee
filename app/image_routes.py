import json
import requests
import os

from app import app
from app import base
from app import db
from app import auth_url

from flask import request, jsonify

from firebase_admin import auth

@app.route('/upload', methods=['POST'])
def upload():
    json_data = request.json
    uid = json_data['uid']
    filename = json_data['filename']

    key = open(os.path.join(os.getcwd(), "app\\web_api_key.txt"), 'r')
    response = requests.post(auth_url,
                    params={"key": key.read()},
                    data=request.json)

    if response.status_code >= 300:
        return response.text, response.status_code
    else:
        return auth.get_user_by_email(email).uid, response.status_code
