import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

APP_ID = os.getenv("app_id")
LAT = 3.0739429
LON = 101.5185278

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

parameters = {
    "lat": LAT,
    "lon": LON,
    "cnt": 4,
    "appid": APP_ID
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Don't forget to bring an ☂️.",
        from_="+19342205364",
        to="+60123460150",
    )
    print(message.status)