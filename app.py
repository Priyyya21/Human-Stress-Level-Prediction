# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

# Load the trained stress prediction model (ideally a Pipeline)
MODEL_PATH = 'stress_model.pkl'   

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read form values one by one (names must match index.html)
        age = float(request.form['Age'])
        gender = request.form['Gender']
        occupation = request.form['Occupation']
        marital_status = request.form['Marital_Status']
        sleep_duration = float(request.form['Sleep_Duration'])
        sleep_quality = float(request.form['Sleep_Quality'])
        wake_up_time = request.form['Wake_Up_Time']        # e.g. "07:30"
        bed_time = request.form['Bed_Time']                # e.g. "23:00"
        physical_activity = float(request.form['Physical_Activity'])
        screen_time = float(request.form['Screen_Time'])
        caffeine_intake = float(request.form['Caffeine_Intake'])
        alcohol_intake = float(request.form['Alcohol_Intake'])
        smoking_habit = request.form['Smoking_Habit']
        work_hours = float(request.form['Work_Hours'])
        travel_time = float(request.form['Travel_Time'])
        social_interactions = float(request.form['Social_Interactions'])
        meditation_practice = request.form['Meditation_Practice']
        exercise_type = request.form['Exercise_Type']
        blood_pressure = float(request.form['Blood_Pressure'])
        cholesterol_level = float(request.form['Cholesterol_Level'])
        blood_sugar_level = float(request.form['Blood_Sugar_Level'])

        # Build a single-row DataFrame with SAME column names as during training
        input_data = pd.DataFrame([{
            'Age': age,
            'Gender': gender,
            'Occupation': occupation,
            'Marital_Status': marital_status,
            'Sleep_Duration': sleep_duration,
            'Sleep_Quality': sleep_quality,
            'Wake_Up_Time': wake_up_time,
            'Bed_Time': bed_time,
            'Physical_Activity': physical_activity,
            'Screen_Time': screen_time,
            'Caffeine_Intake': caffeine_intake,
            'Alcohol_Intake': alcohol_intake,
            'Smoking_Habit': smoking_habit,
            'Work_Hours': work_hours,
            'Travel_Time': travel_time,
            'Social_Interactions': social_interactions,
            'Meditation_Practice': meditation_practice,
            'Exercise_Type': exercise_type,
            'Blood_Pressure': blood_pressure,
            'Cholesterol_Level': cholesterol_level,
            'Blood_Sugar_Level': blood_sugar_level
        }])

        # Predict with the loaded model
        prediction = model.predict(input_data)

        # If model outputs numeric labels 0/1/2, map them to text
        stress_map = {
            0: "Low Stress",
            1: "Medium Stress",
            2: "High Stress"
        }

        pred_raw = prediction[0]
        # Handle both numeric and string outputs safely
        if isinstance(pred_raw, (int, np.integer)):
            output = stress_map.get(int(pred_raw), "Unknown")
        else:
            # e.g. model already returns 'Low'/'Medium'/'High'
            output = str(pred_raw)

        return render_template(
            'index.html',
            prediction_text=f'Predicted Stress Level: {output}'
        )

    except Exception as e:
        # Helpful error display while debugging
        return render_template(
            'index.html',
            prediction_text=f'Error during prediction: {e}'
        )


if __name__ == "__main__":
    app.run(debug=True)
