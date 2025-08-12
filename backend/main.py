# main.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://storage.googleapis.com", "https://storage.cloud.google.com", "*"])

@app.route('/status')
def status():
    return jsonify({'status': 'Backend is running !'})

@app.route('/')
def home():
    return "Hello from Flask backend on GCP!"

@app.route('/health')
def health():
    return jsonify({"health": "OK", "service": "Backend Service"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)