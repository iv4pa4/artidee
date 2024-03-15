from app import app, db
from flask import jsonify

@app.route('/friends/<user_id>', methods=['GET'])
def get_friends(user_id):
    
    connections_ref = db.collection("Connections")
    friends = []
    
    query = connections_ref.where("user_id_1", "==", user_id).get()
    for doc in query:
        friend_id = doc.to_dict()["user_id_2"]
        friends.append(friend_id)

    query = connections_ref.where("user_id_2", "==", user_id).get()
    for doc in query:
        friend_id = doc.to_dict()["user_id_1"]
        friends.append(friend_id)
    
    return jsonify({'friends': friends})
