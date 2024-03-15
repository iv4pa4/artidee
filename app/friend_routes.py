from app import app, base, db
from flask import request, jsonify
from firebase_admin import auth

@app.route('/add_friend', methods=['POST'])
def add_friend():
    query = db.collection("Blacklist")
    docs = query.stream()
    uids = []
    for doc in docs:
        uids.append(doc.get('user_id'))

    for uid in uids:
        if auth.get_user(uid).display_name == request.json['name']:
            query = db.collection("Connections").where('user_id_1', '==', request.json['user_id'])
            docs = query.stream()
            query = db.collection("Connections").where('user_id_2', '==', request.json['user_id'])
            docs2 = query.stream()
            curr_friends = []

            for doc in docs:
                curr_friends.append(doc.get('user_id_2'))
            for doc in docs2:
                curr_friends.append(doc.get('user_id_1'))

            if uid in curr_friends:
                return jsonify({"message": "Friend already in list"}), 200

            update_time, doc_id = db.collection("Connections").add({"user_id_1": request.json['user_id'], "user_id_2": uid})
            return jsonify({"message": "Friend added successfully"}), 200

@app.route('/friends', methods=['GET'])
def get_friends():
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'Missing parameters'}), 400

    connections_ref = db.collection("Connections")
    friends = []
    names = []

    query = connections_ref.where("user_id_1", "==", user_id).get()
    for doc in query:
        friend_id = doc.to_dict()["user_id_2"]
        friends.append(friend_id)
        names.append(auth.get_user(friend_id).display_name)

    query = connections_ref.where("user_id_2", "==", user_id).get()
    for doc in query:
        friend_id = doc.to_dict()["user_id_1"]
        friends.append(friend_id)
        names.append(auth.get_user(friend_id).display_name)

    return jsonify({'friends': friends, 'names': names})
