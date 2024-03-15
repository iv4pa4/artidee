import json
import requests
import os

from app import app
from app import base
from app import auth_url
from app import db

from flask import request, jsonify

from firebase_admin import auth
from firebase_admin.auth import UserRecord

@app.route('/add', methods=['POST'])
def add():
    query = db.collection("Blacklist")
    docs = query.stream()
    uids = []
    for doc in docs:
        uids.append(doc.get('user_id'))

    for uid in uids:
        if auth.get_user(uid).display_name == request.json['name']:
            query = db.collection("Connections").where('user_id_1', '==', request.json['user_id'])
            docs = query.stream()
            curr_friends = []
            for doc in docs:
                curr_friends.append(doc.get('user_id_2'))
            if uid in curr_friends:
                return jsonify({"message": "Friend already in list"}), 200
            update_time, doc_id = db.collection("Connections").add({"user_id_1": request.json['user_id'], "user_id_2": uid})
            return jsonify({"message": "Friend added successfully"}), 200

    return jsonify({"message": "Friend name not found"}), 404