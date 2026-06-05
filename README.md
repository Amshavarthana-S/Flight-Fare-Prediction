# Flight Fare Prediction System

## Overview

This project predicts flight ticket prices using Machine Learning. The model is trained using historical flight data and predicts ticket fares based on flight details.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML

## Machine Learning Model

Random Forest Regressor was used to train the model.

## Dataset

The dataset contains:

* Airline
* Source
* Destination
* Journey Date
* Duration
* Total Stops
* Departure Time
* Price

## Features

* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Machine Learning Prediction
* Flask Web Interface

## Model Performance

* R² Score: 0.81
* MAE: 1178
* MAPE: 13.3%

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run Flask application

python app.py

3. Open browser

http://127.0.0.1:5000/
