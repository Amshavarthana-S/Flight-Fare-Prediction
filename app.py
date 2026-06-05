from flask import Flask, render_template, request
import pickle
import numpy as np
from datetime import datetime
import re

app = Flask(__name__)

model = pickle.load(open('rd_random.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Basic Inputs
    destination = int(request.form['destination'])
    total_stops = int(request.form['total_stops'])
    airlines = int(request.form['airlines'])

    # Journey Date
    journey_date = request.form['journey_date']
    journey_date = datetime.strptime(
        journey_date,
        "%Y-%m-%d"
    )

    journey_day = journey_date.day
    journey_month = journey_date.month

    # Departure Time
    departure_time = request.form['departure_time']

    dep_hour, dep_minute = map(
        int,
        departure_time.split(":")
    )

    # Duration Example: 2h 30m
    duration = request.form['duration']

    hour_match = re.search(r'(\d+)h', duration)
    minute_match = re.search(r'(\d+)m', duration)

    duration_hour = int(hour_match.group(1)) if hour_match else 0
    duration_minute = int(minute_match.group(1)) if minute_match else 0

    # Calculate Arrival Time Automatically
    total_minutes = (
        dep_hour * 60 +
        dep_minute +
        duration_hour * 60 +
        duration_minute
    )

    arrival_hour = (total_minutes // 60) % 24
    arrival_minute = total_minutes % 60

    # Source Encoding
    source = request.form['source']

    source_banglore = 1 if source == "banglore" else 0
    source_chennai = 1 if source == "chennai" else 0
    source_delhi = 1 if source == "delhi" else 0
    source_kolkata = 1 if source == "kolkata" else 0
    source_mumbai = 1 if source == "mumbai" else 0

    # Airline Encoding
    airline_air_india = 1 if airlines == 7 else 0
    airline_goair = 1 if airlines == 4 else 0
    airline_indigo = 1 if airlines == 3 else 0
    airline_jet = 1 if airlines == 10 else 0
    airline_jet_business = 1 if airlines == 11 else 0
    airline_multiple = 1 if airlines == 8 else 0
    airline_multiple_premium = 1 if airlines == 9 else 0
    airline_spicejet = 1 if airlines == 1 else 0
    airline_trujet = 1 if airlines == 0 else 0
    airline_vistara = 1 if airlines == 5 else 0
    airline_vistara_premium = 1 if airlines == 6 else 0

    features = np.array([[
        destination,
        total_stops,
        journey_day,
        journey_month,
        arrival_hour,
        arrival_minute,
        dep_hour,
        dep_minute,
        duration_hour,
        duration_minute,
        source_banglore,
        source_chennai,
        source_delhi,
        source_kolkata,
        source_mumbai,
        airlines,
        airline_air_india,
        airline_goair,
        airline_indigo,
        airline_jet,
        airline_jet_business,
        airline_multiple,
        airline_multiple_premium,
        airline_spicejet,
        airline_trujet,
        airline_vistara,
        airline_vistara_premium
    ]])

    prediction = model.predict(features)[0]

    return render_template(
        'index.html',
        prediction_text=
        f'Estimated Flight Fare: ₹ {round(prediction, 2)}'
    )


if __name__ == "__main__":
    app.run(debug=True)