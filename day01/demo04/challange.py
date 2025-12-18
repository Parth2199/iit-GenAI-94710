import requests

api_key = "f5fbf3d88546b398a1e0e56b97b1b45b"

city = input("Enter city name: ")
url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": city,"appid": api_key,"units": "metric"}

try:
    r = requests.get(url, params=params, timeout=8)
    r.raise_for_status()
    j = r.json()

    main = j.get("main", {})
    wind = j.get("wind", {})
    weather_desc = j.get("weather", [{}])[0].get("description", "")

    print(f"\nWeather for {city.title()}:")
    print(f"  Description : {weather_desc}")
    print(f"  Temperature : {main.get('temp')} °C")
    print(f"  Feels like  : {main.get('feels_like')} °C")
    print(f"  Humidity    : {main.get('humidity')}%")
    print(f"  Wind speed  : {wind.get('speed')} m/s")

except requests.HTTPError:
    if r.status_code == 404:
        print("City not found. Check spelling.")
    else:
        print("HTTP error:", r.status_code,r.text) 