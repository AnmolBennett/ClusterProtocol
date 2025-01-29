# ClusterProtocol

# BTC Price Prediction API
🚀 A Machine Learning-powered API to predict the next day's closing price of Bitcoin (BTC) based on historical price data.


# 📌 Project Overview
This project leverages Regression and Deep Learning models to predict Bitcoin's closing price using historical data. The trained models are deployed as a REST API using Flask, allowing users to make real-time predictions.


# 📂 Project Structure
'''
BTC-Price-Prediction/
│── data/               # Contains raw and preprocessed datasets
│── model/              # Trained models (Linear Regression, Random Forest, XGBoost, LSTM)
│── api/                # Flask API implementation
│── requirements.txt    # Python dependencies
│── README.md           # Documentation
│── btc_price_prediction.py  # Main script for training & API deployment
'''


# 🚀 Steps to Run the Project
1️⃣ Install Dependencies
Ensure Python 3.8+ is installed, then install required packages:
*Command*: pip install -r requirements.txt

2️⃣ Download and Preprocess Data
Run the following script to fetch Bitcoin data and preprocess it:
*Command*: python btc_price_prediction.py
This will generate the preprocessed dataset inside the data/ directory.

3️⃣ Train Models
To train all models and save them:
*Command*: python btc_price_prediction.py
Trained models will be stored inside the model/ directory.

4️⃣ Run the Flask API 
Start the Flask API server:
*Command*: python btc_price_prediction.py
Once running, the API will be available at:
http://127.0.0.1:5000/


# 🖥 API Usage Details
📌 1. Check API Status
=
Endpoint: /
Method: GET
Response:
{
    "message": "BTC Price Prediction API is running. Use /predict endpoint for predictions."
}
📌 2. Make a Prediction
=
Endpoint: /predict
Method: POST
Content-Type: application/json
Request Body Example:

json
Copy
Edit
{
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
Response Example:

json
Copy
Edit
{
    "Linear Regression Prediction": 45000.5,
    "Random Forest Prediction": 45200.8,
    "XGBoost Prediction": 45120.7,
    "LSTM Prediction": "LSTM model not available"
}
Error Handling:

If required fields are missing, API returns a 400 error.
If any internal error occurs, API returns a 500 error.


# 🧠 Summary of Approach
📊 Data Preprocessing

Fetched historical BTC price data from Yahoo Finance.
Engineered features like Moving Averages, Volatility, and RSI.
Normalized numerical features for better model performance.
📈 Model Development

Trained multiple models:
Linear Regression
Random Forest
XGBoost
LSTM (Deep Learning)
Evaluated models using MSE, MAE, and RMSE.
Selected Random Forest as the best model based on performance.


# 🌍 Model Deployment as API
Developed a Flask API for real-time predictions.
Implemented error handling and input validation.
Designed the API to return predictions from all trained models.


# 🚀 Future Improvements
✅ Deploy API on Heroku / AWS / Render
✅ Add Frontend UI using React.js
✅ Improve model accuracy using advanced time-series models


# 👨‍💻 Author & Contribution
✉️ If you have any suggestions or feedback, feel free to contribute or contact me!

🔗 GitHub Repo: [Insert your GitHub Repository Link]
