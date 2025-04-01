from flask import Flask, request, render_template,jsonify
import numpy as np

import pickle
import json
import os

# importing model
model = pickle.load(open('model.pkl','rb'))
sc=pickle.load(open('standard.pkl','rb'))
ms = pickle.load(open('minmaxscaler.pkl','rb'))

# creating flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/contact')
def contact():
    # Render second.html
    return render_template('contact.html')

@app.route('/about')
def about():
    # Render second.html
    return render_template('about.html')

@app.route('/recommendationPage')
def recommendationPage():
    # Render second.html
    return render_template('recommendationPage.html')

@app.route("/predict",methods=['POST'])
def predict():
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosphorus'])
    K = int(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])
    frost_risk=float(request.form['Frost_risk'])

    feature_list = [N, P, K, temp, humidity, ph, rainfall,frost_risk]
    single_pred = np.array(feature_list).reshape(1, -1)
    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    
    prediction = model.predict(final_features)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Black gram", 17: "Mung bean", 18: "Moth beans",
                 19: "Pigeon peas", 20: "Kidney beans", 21: "Chickpea", 22: "Coffee"}
    result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    if prediction[0] in crop_dict:
        crop_name = crop_dict[prediction[0]]
        file_path = os.path.join(os.path.dirname(__file__), 'crop_data.json')

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return jsonify(result="Error: crop_data.json not found")

        # Function to fetch crop data by crop name
        def get_crop_data(crop_name):
            crop_name = crop_name.lower()
            if crop_name in data:
                return data[crop_name]
            else:
                return None

        crop = get_crop_data(crop_name)

        if crop:
            result = {
                "name": crop['name'],
                "description": crop['description'],
                "season": crop['season'],
                "yield": crop['average_yield_per_hectare'],
                "region": crop['region'],
                "image_filename": crop['image_filename']
            }
        else:
            print(f"{crop_name} not found in the data.")

    return jsonify(result= result)


# python main
if __name__ == "__main__":
    app.run(port=5005)
