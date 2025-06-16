from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

statuses = {}

@app.route('/update', methods=['POST'])
def update_status():
    data = request.get_json()
    statuses[data['city']] = data['status']
    return jsonify({"message": "Status updated"})

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(statuses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
