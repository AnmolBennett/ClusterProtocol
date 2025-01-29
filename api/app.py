import numpy as np
from flask import Flask, request, jsonify
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load models
lin_reg = joblib.load(r"C:\Users\kanmo\OneDrive\Desktop\Cluster Protocol\model\linear_regression_model.pkl")
rf_reg = joblib.load(r"C:\Users\kanmo\OneDrive\Desktop\Cluster Protocol\model\random_forest_model.pkl")
xgb_reg = joblib.load(r"C:\Users\kanmo\OneDrive\Desktop\Cluster Protocol\model\xgboost_model.pkl")

try:
    lstm_model = load_model(r"C:\Users\kanmo\OneDrive\Desktop\Cluster Protocol\model\lstm_model.h5")
except Exception as e:
    lstm_model = None
    print(f"Error loading LSTM model: {e}")

# Initialize Flask app
app = Flask(__name__)

# Home route for testing
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Bitcoin Price Prediction API! Use the /predict endpoint with a POST request."

# Prediction route (supports both GET and POST)
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        # Return instructions for using the API
        return """
        Welcome to the Bitcoin Price Prediction API!<br><br>
        To get predictions, send a POST request to this endpoint with the following JSON payload:<br><br>
        {
            "Open": 0.5,
            "High": 0.6,
            "Low": 0.4,
            "Volume": 0.7,
            "Adj Close": 0.55,
            "7-day MA": 0.52,
            "30-day MA": 0.53,
            "7-day Volatility": 0.02,
            "30-day Volatility": 0.03,
            "RSI": 0.65
        }
        """

    elif request.method == 'POST':
        try:
            # Get JSON payload from request
            data = request.get_json()

            # Check if all required fields are present
            required_fields = [
                'Open', 'High', 'Low', 'Volume', 'Adj Close',
                '7-day MA', '30-day MA', '7-day Volatility', '30-day Volatility', 'RSI'
            ]
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Missing required field: {field}"}), 400

            # Extract features from payload
            features = [
                data['Open'],
                data['High'],
                data['Low'],
                data['Volume'],
                data['Adj Close'],
                data['7-day MA'],
                data['30-day MA'],
                data['7-day Volatility'],
                data['30-day Volatility'],
                data['RSI']
            ]
            features = np.array(features).reshape(1, -1)

            # Make predictions with each model
            lin_reg_pred = lin_reg.predict(features)[0]
            rf_reg_pred = rf_reg.predict(features)[0]
            xgb_reg_pred = xgb_reg.predict(features)[0]

            # LSTM Prediction if model is available
            lstm_pred = None
            if lstm_model:
                lstm_features = features.reshape(1, 1, features.shape[1])
                lstm_pred = lstm_model.predict(lstm_features)[0][0]

            # Return predictions as JSON
            response = {
                "Linear Regression Prediction": lin_reg_pred,
                "Random Forest Prediction": rf_reg_pred,
                "XGBoost Prediction": xgb_reg_pred,
                "LSTM Prediction": lstm_pred if lstm_pred is not None else "LSTM model not available"
            }
            return jsonify(response)

        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "Open": 1,
    "High": 2,
    "Low": 1,
    "Volume": 1000,
    "Adj Close": 2,
    "7-day MA": 1.5,
    "30-day MA": 1.6,
    "7-day Volatility": 0.1,
    "30-day Volatility": 0.2,
    "RSI": 50
}

response = requests.post(url, json=data)
print(response.json())  # Print the response from the API
