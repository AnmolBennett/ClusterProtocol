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
