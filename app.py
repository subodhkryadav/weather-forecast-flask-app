from flask import Flask, render_template, request
import pickle
import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Load models
with open("model/current_model.pkl", "rb") as f:
    ml_model = pickle.load(f)

with open("model/prophet_model.pkl", "rb") as f:
    prophet_model = pickle.load(f)

app = Flask(__name__)

def get_live_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    res = requests.get(url)
    return res.json()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form['city']
        weather = get_live_weather(city)

        # Extract features
        humidity = weather['current']['humidity']
        wind = weather['current']['wind_kph']

        # Predict today's temperature
        today_temp = ml_model.predict([[humidity, wind]])[0]

        # Predict next 7 days using Prophet
        future = prophet_model.make_future_dataframe(periods=7)
        forecast = prophet_model.predict(future)
        next_day = round(forecast.iloc[-7]["yhat"], 2)
        day_after = round(forecast.iloc[-6]["yhat"], 2)
        week = forecast[["ds", "yhat"]].tail(7).to_dict(orient="records")
        month_avg = round(forecast["yhat"].mean(), 2)

        return render_template("index.html",
            weather=weather,
            today_pred=round(today_temp, 2),
            next_day_pred=next_day,
            day_after_pred=day_after,
            forecast=week,
            month_avg=month_avg)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)