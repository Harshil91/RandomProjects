import requests
import smtplib
from email.message import EmailMessage

API_KEY = "your_openweathermap_api_key"
EMAIL_ADDRESS = "your_email_address"
EMAIL_PASSWORD = "your_email_password"

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def send_email(weather_info, city):
    msg = EmailMessage()
    msg.set_content(f"Weather update for {city}: {weather_info}")

    msg["Subject"] = f"Weather Update for {city}"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    city = "San Francisco"
    weather_data = get_weather_data(city)
    weather_info = f"{weather_data['weather'][0]['description'].capitalize()}, {weather_data['main']['temp']}°C"
    send_email(weather_info, city)

if __name__ == "__main__":
    main()
