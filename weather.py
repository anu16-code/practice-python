import requests
api_key = "1c7309b530e4ad919c38fad8f9b55759"
def get_weather(City):
    url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data= response.json()
        main = data['main']
        temperatue = main['temp']
        humidity = main['humidity']
        weather_desc = data['weather'][0]['description']
        print(f"Temperatue: {temperatue}°C")
        print(f"Humidity: {humidity}%")
        print(f"weather description: {weather_desc}")
    else:
        print("Error Fetching weather data")

if __name__ == "__main__":
    city = input("Enter city name:")
    get_weather(city)
