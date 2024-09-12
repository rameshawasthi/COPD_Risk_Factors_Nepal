import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import os


app = Flask(__name__)

# Set paths for model and encoder files
model_path = os.path.join(os.getcwd(), 'Best_Random_Forest_Model.pkl')
encoder_path = os.path.join(os.getcwd(), 'encoder.pkl')

# Load the trained model 
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    raise FileNotFoundError(f"Model file not found: {model_path}")


def preprocess_input(data):
    input_data = pd.DataFrame([data])

    categorical_columns = ['Gender', 'Smoking_Status', 'Location']

    if os.path.exists(encoder_path):
        with open(encoder_path, 'rb') as f:
            encoder = pickle.load(f)
    else:
        raise FileNotFoundError(f"Encoder file not found: {encoder_path}")

    input_encoded = encoder.transform(input_data[categorical_columns])

    
    if not isinstance(input_encoded, np.ndarray): 
        input_encoded = input_encoded.toarray() 

    input_encoded_df = pd.DataFrame(input_encoded, columns=encoder.get_feature_names_out(categorical_columns))

   
    input_data = input_data.drop(categorical_columns, axis=1)
    input_data = input_data.join(input_encoded_df)

    return input_data


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
   
    input_data = {
        'Age': request.form['age'],
        'Gender': request.form['gender'],
        'Smoking_Status': request.form['smoking_status'],
        'Biomass_Fuel_Exposure': request.form['biomass_fuel_exposure'],
        'Occupational_Exposure': request.form['occupational_exposure'],
        'Family_History_COPD': request.form['family_history_copd'],
        'BMI': request.form['bmi'],
        'Location': request.form['location'],
        'Air_Pollution_Level': request.form['air_pollution_level'],
        'Respiratory_Infections_Childhood': request.form['respiratory_infections_childhood']
    }

  
    processed_data = preprocess_input(input_data)

   
    prediction = model.predict(processed_data)

  
    output = 'COPD Positive' if prediction[0] == 1 else 'COPD Negative'
    return render_template('index.html', prediction_text=f'Predicted Outcome: {output}')


if __name__ == "__main__":
    app.run(debug=True)
