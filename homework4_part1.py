import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


CITY = "Dnipro"

URL = "https://api.open-meteo.com/v1/forecast?latitude=48.45&longitude=34.98&current_weather=true"

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    temperature REAL
)
""")

conn.commit()


def get_temperature():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        temperature = data["current_weather"]["temperature"]

        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        return current_date, current_time, temperature
    else:
        print("Помилка отримання даних")
        return None

def save_to_db(date, time_value, temperature):
    cursor.execute("""
    INSERT INTO weather (date, time, temperature)
    VALUES (?, ?, ?)
    """, (date, time_value, temperature))

    conn.commit()


print("Програма запущена...")
print("Оновлення кожні 30 хвилин")

while True:
    weather_data = get_temperature()

    if weather_data:
        date, time_value, temperature = weather_data

        save_to_db(date, time_value, temperature)

        print(f"[{date} {time_value}] Температура: {temperature}°C")

    time.sleep(1800)