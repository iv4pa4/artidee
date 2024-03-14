from app import app

@app.route('/topic', methods=['POST'])
def get_topic():
    return "Artidee"