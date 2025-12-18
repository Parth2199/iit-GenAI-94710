import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("OPEN_WEATHER_API")

flag='yes'if api_key else 'no' 
print("Api key Loaded !!")

city=input("Enter City : ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
weather=response.json()
#print("Weather : ",weather )
print("Temperature: ", weather["main"]["temp"])
