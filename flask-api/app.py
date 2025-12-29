from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        "msg": "Greetings from the Backend! This data was sent to you by Pyhton Flask 🐍/n Without any typos!",
        "status": "success"
    })

#Minor formatting patch
@app.route('/api/hello2', methods=['GET'])
def hello2():
    return jsonify({
        "msg": "Hello2 from Backend (minor feature)!",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

