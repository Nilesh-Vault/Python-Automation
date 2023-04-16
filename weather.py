# 12eed360fdd752b42302b6b50c1f9eb1
# prak was also here
import requests

API_KEY = '12eed360fdd752b42302b6b50c1f9eb1'

Base_url = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")

request_url = f"{Base_url}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data =  response.json()
    weather = data['weather'][0]['description']
    print(f"Weather: {weather}")
    temperature = data['main']['temp']
    print("Temperature:",round(temperature-273.15,2),"celsius")
else:
    print("An error occurred")