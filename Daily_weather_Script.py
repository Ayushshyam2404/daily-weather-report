import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Load from environment
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT")
API_KEY = os.getenv("OPENWEATHER_API")

CITY = "Jamshedpur"  # change to your city
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather
response = requests.get(URL)
data = response.json()

if data.get("cod") != 200:
    raise Exception(f"Error fetching weather: {data.get('message')}")

weather = data["weather"][0]["description"].title()
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
wind = data["wind"]["speed"]
date = datetime.now().strftime("%A, %d %B %Y")

# Build email
subject = f"Daily Weather Report - {CITY} ({date})"
html = f"""
<html>
  <body style="font-family: Arial, sans-serif;">
    <h2>🌤 Weather Report for {CITY}</h2>
    <p><b>Date:</b> {date}</p>
    <p><b>Condition:</b> {weather}</p>
    <p><b>Temperature:</b> {temp}°C (Feels like {feels_like}°C)</p>
    <p><b>Humidity:</b> {humidity}%</p>
    <p><b>Wind Speed:</b> {wind} m/s</p>
  </body>
</html>
"""

msg = MIMEMultipart("alternative")
msg["From"] = EMAIL
msg["To"] = RECIPIENT
msg["Subject"] = subject
msg.attach(MIMEText(html, "html"))

with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.sendmail(EMAIL, RECIPIENT, msg.as_string())
