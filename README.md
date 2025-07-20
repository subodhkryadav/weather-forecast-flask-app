# 🌤️ Weather Forecasting Web App

A real-time and predictive weather forecasting web application built using **Flask**, **Python**, and **Machine Learning**. It provides accurate weather data for today, tomorrow, and the coming week using a combination of **WeatherAPI**, custom-trained ML models, and **Prophet** for time-series forecasting.

---

## 🔥 Key Features

- 🌐 Real-time weather info via WeatherAPI
- 📊 Today’s temperature prediction using ML
- ⏭️ Tomorrow + Day-after prediction via Prophet
- 📅 7-day temperature forecast with graph
- 🗓️ Current month's average temperature

---

## 🧠 Tech Stack

| Layer        | Tools / Libraries                                  |
|--------------|----------------------------------------------------|
| Backend      | Flask, Python                                       |
| Machine Learning | Scikit-learn, Prophet (Facebook), Pandas         |
| API          | WeatherAPI (www.weatherapi.com)                    |
| Frontend     | HTML, CSS, Jinja2 Templates                         |
| Utilities    | dotenv (for API key security), requests             |

---

## 📁 Project Structure

weather-forecast-app/
├── app.py # Flask application entry point
├── .env # API Key (kept secret)
├── requirements.txt # All dependencies
│
├── /data/
│ └── Cleaned_indian_weather_history.csv
│
├── /model/
│ ├── current_model.pkl
│ └── prophet_model.pkl
│
└── /templates/
└── index.html # Main UI template


---

## 🚀 Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/subodhkryadav/weather-forecast-flask-app.git
cd weather-forecast-flask-app

🔐 2. Create a .env File
Create a .env file and add your WeatherAPI key:
WEATHER_API_KEY=your_actual_api_key_here

📦 3. Install Required Libraries
pip install -r requirements.txt
Or manually:

pip install flask requests pandas scikit-learn prophet python-dotenv


▶️ 4. Run the App
python app.py
Now open your browser at http://127.0.0.1:5000

Home Page with current weather

Prediction section with charts

7-day and Monthly insights

👨‍💻 About Me
Subodh Kumar Yadav
📍 Madhubani, Bihar | 🎓 B.Tech CSE @ Jagannath University, Jaipur
🔗 LinkedIn:-https://www.linkedin.com/in/subodh-kumar-yadav-522828293/
💻 GitHub:- https://github.com/subodhkryadav

📄 License
This project is open-source under the MIT License.
