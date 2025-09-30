from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
import os


app = Flask(__name__)
Model1= 'model.pkl'

@app.route("/", methods=["GET"])
def home():
    return "Weather Forecasting Backend is running!"

@app.route("/train", methods=["POST"])
def trian_model():
    file = request.files['file']
    df = pd.read_csv(file)
    target_column = "temperature"
    feature_columns = ['humidity', 'pressure', 'wind_speed', 'rainfall', 'cloud_cover']
    if not set(feature_columns + [target_column]).issubset(df.columns):
        return jsonify({"error": "Dataset missing required columns"})
    
    X = df[feature_columns]
    y = df[target_column]

    model = LinearRegression()
    model.fit(X,y)

    pickle.dump(model,open(Model1,'wb'))

    return jsonify({'message':'Model trained successfuly.'})

@app.route("/test", methods=["POST"])
def test_model ():
    file = request.files['file']
    df = pd.read_csv(file)

    target_column = "temperature"
    feature_columns = ['humidity', 'pressure', 'wind_speed', 'rainfall', 'cloud_cover']
    X_test = df[feature_columns]
    y_test = df[target_column]
    if 'file' not in request.files:
        return jsonify({'Error':'Please uploade the file'}) ,400

    if not set(feature_columns + [target_column]).issubset(df.columns):
        return jsonify({"error": "Dataset missing required columns"}), 400
    
    model = pickle.load(open(Model1,'rb'))
    y_predict = model.predict(X_test)
    mse = mean_squared_error(y_test,y_predict)

    return jsonify({'mse':mse})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    model = pickle.load(open(Model1,'rb'))
    X_input = [data['features']]
    yp = model.predict(X_input)[0]

    return jsonify({'Prediction': yp})

if __name__== "__main__":
    app.run(debug=True)
    



    