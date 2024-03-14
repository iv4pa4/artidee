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
    update_time, doc_id = db.collection("Images").add({"filename": request.json['filename'], "user_id": request.json['user_id']})
    return jsonify({"message": doc_id.id}), 200

@app.route('/get_gallery', methods=['POST'])
def get_gallery():
    query = db.collection("Images").where('user_id', '==', request.json['user_id'])
    docs = query.stream()
    jsons = []
    for doc in docs:
        jsons.append(doc.get('filename'))
    return json.dumps(jsons), 200