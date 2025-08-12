# main.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/status')
def status():
    return jsonify({'status': 'Backend is running !'})

@app.route('/')
def home():
    return "Hello from Flask backend on GCP!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)