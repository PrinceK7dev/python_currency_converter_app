from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow requests from Flutter

# Endpoint to get all available currencies
@app.route('/currencies', methods=['GET'])
def get_currency_list():
    try:
        response = requests.get("https://api.frankfurter.app/currencies")
        data = response.json()
        return jsonify(sorted(data.keys()))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to convert currency
@app.route('/convert', methods=['POST'])
def convert_currency():
    try:
        data = request.get_json()
        from_curr = data['from']
        to_curr = data['to']
        amount = float(data['amount'])

        rates_resp = requests.get("https://api.frankfurter.app/latest")
        rates = rates_resp.json()['rates']
        rates['EUR'] = 1.0  # base

        if from_curr not in rates or to_curr not in rates:
            return jsonify({"error": "Currency not supported!"}), 400

        eur_amount = amount / rates[from_curr]
        result = eur_amount * rates[to_curr]

        return jsonify({
            "from": from_curr,
            "to": to_curr,
            "amount": amount,
            "converted": round(result, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
