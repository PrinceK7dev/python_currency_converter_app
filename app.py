from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

API_KEY = "mysecretkey"  # You can load from env instead

@app.before_request
def check_api_key():
    if request.endpoint == 'index':
        return  # Allow root access
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/')
def index():
    return "Currency Converter API is running!"

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    from_currency = data.get('from')
    to_currency = data.get('to')
    amount = float(data.get('amount', 0))

    # Dummy conversion
    result = amount * 82.5  # Replace with real API
    return jsonify({"converted_amount": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
