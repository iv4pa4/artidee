import json
import time

from app import app, base, db

from flask import request, jsonify

@app.route('/upload', methods=['POST'])
def upload():
    _, doc_id = db.collection("Images").add({"filename": request.json['filename'], "user_id": request.json['user_id'], "timestamp": int(time.time())})
    return jsonify({"message": doc_id.id}), 200

@app.route('/get_gallery', methods=['POST'])
def get_gallery():
    query = db.collection("Images").where('user_id', '==', request.json['user_id']).order_by("timestamp", "DESCENDING")
    docs = query.stream()
    jsons = []
    print(docs)
    for doc in docs:
        jsons.append(doc.get('filename'))
    return jsonify({"message": jsons}), 200