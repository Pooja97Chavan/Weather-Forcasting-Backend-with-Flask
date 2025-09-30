# Weather-Forcasting-Backend-with-Flask
A simple Flask backend for weather forecasting using a Linear Regression model. Users can retrain, test, and predict temperature using CSV files or JSON input.
Features:
Train API – You can upload CSV file to train (or retrain) the model.
Test API – You can upload CSV file to test model and get Mean Squared Error (MSE).
Predict API – Send JSON data to get predicted temperature.

Your dataset must contains following columns:
timestamp, temperature, humidity, pressure, wind_speed, rainfall, cloud_cover
From these columns-
Target: temperature
Features: humidity, pressure, wind_speed, rainfall, cloud_cover
timestamp column is ignored for training.
