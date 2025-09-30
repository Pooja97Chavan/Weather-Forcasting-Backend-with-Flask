Weather Forecasting Backend with Flask

A simple Flask backend for weather forecasting using a Linear Regression model. Users can train, test, and predict temperature using CSV files or JSON input.

Features
Train API – Upload CSV file to train (or retrain) the model.
Test API – Upload CSV file to test model and get Mean Squared Error (MSE).
Predict API – Send JSON data to get predicted temperature.

Dataset
The dataset should contain the following columns:
timestamp, temperature, humidity, pressure, wind_speed, rainfall, cloud_cover
Target: temperature
Features: humidity, pressure, wind_speed, rainfall, cloud_cover
timestamp column is ignored for training.

Installation
Clone the repository:
git clone <your-repo-url>
cd <repo-folder>

Install dependencies:
pip install -r requirements.txt

Run the backend:
python app.py
Server runs at http://127.0.0.1:5000/.

API Usage
1️⃣ Train Model
POST http://127.0.0.1:5000/train
Body → form-data → key=file → upload CSV
Response:
{"message": "Model trained successfully"}

2️⃣ Test Model
POST http://127.0.0.1:5000/test
Body → form-data → upload CSV
Response:
{"mse": 3.21}

3️⃣ Predict Temperature
POST http://127.0.0.1:5000/predict
Body → raw → JSON:
{
  "features": [65, 1010, 4, 1, 75]
}
Response:
{"prediction": 29.4}

Notes
pickle is used to save/load the trained model. No need to install separately.
Use Postman Desktop App or Postman Desktop Agent to send requests to localhost.
