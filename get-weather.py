import requests

API_KEY = "369769cd00b7f041d4631c4bda8aa3e1"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]["description"]
        temperature = main["temp"]
        humidity = main["humidity"]

        print(f"City: {city}")
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or error in fetching data.")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
