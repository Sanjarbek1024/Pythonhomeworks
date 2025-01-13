import requests

# OpenWeatherMap API datas
API_key = "bd01cd3b7d6f889b94b73032812414eb"  # My API key
BASE_url = "https://api.openweathermap.org/data/2.5/weather"

# Requesting "Tashkent"
city = "Tashkent"
params = {
    "q": city,
    "appid": API_key,
    "units": "metric",  # Temperature in Celcius
}

# Requests
response = requests.get(BASE_url, params=params)

if response.status_code == 200:  # If true
    data = response.json()
    # Showing the important datas
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather}")
else:
    print("Error was occured")


