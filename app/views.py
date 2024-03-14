from app import app

@app.route('/topic', methods=['GET'])
def get_topic():
    return "Artidee"