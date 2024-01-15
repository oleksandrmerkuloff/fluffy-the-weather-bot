import requests

import os

API_KEY = os.getenv("API_TOKEN")


def weather_report(weather: dict) -> tuple:
    message = ""
    for name, data in weather.items():
        if name == "Опади":
            image = data
        message += f"{name}: {data}\n"
    return image, message.strip()


def data_cleaner(weather: dict) -> dict:
    current_weather = {}
    current_weather["Опади"] = weather["weather"][0]["main"]
    current_weather["Температура, °C"] = int(weather["main"]["temp"])
    current_weather["Відчувається як, °C"] = int(weather["main"]["feels_like"])
    current_weather["Тиск, мм"] = weather["main"]["pressure"]
    current_weather["Вологість, %"] = weather["main"]["humidity"]
    current_weather["Вітер, м/сек"] = round(weather["wind"]["speed"], 1)
    return weather_report(current_weather)


def geocoding(city: str) -> tuple:
    api_link = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"q": city, "appid": API_KEY}
    response = requests.get(api_link, params=params).json()[0]
    lat, lon = response["lat"], response["lon"]
    return get_current_weather_data((lat, lon,))


def get_current_weather_data(coordinates: tuple):
    api_link = "https://api.openweathermap.org/data/2.5/weather"
    lat = coordinates[0]
    lon = coordinates[1]
    params = {"lat": lat, "lon": lon, "units": "metric", "appid": API_KEY}
    response = requests.get(api_link, params=params)
    return data_cleaner(response.json())


# def get_three_hour_weather_data(coordinates: tuple):
#     api_link = "https://api.openweathermap.org/data/2.5/forecast"
#     lat = coordinates[0]
#     lon = coordinates[1]
#     params = {"lat": lat, "lon": lon, "units": "metric", "appid": API_KEY}
#     response = requests.get(api_link, params=params)
#     print(response.json())


if __name__ == "__main__":
    coordinates = geocoding("Киев")
    print(get_current_weather_data(coordinates))
    # get_three_hour_weather_data(coordinates)
