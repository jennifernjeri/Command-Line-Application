API_KEY = "a79a93337a0a7606914b3de6f9e3fe1b"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

import requests

def main():

    city = input("Please enter city name:")

    url = BASE_URL.format(city, API_KEY)

    data = requests.get(url).json()

    city_name = data['name']

    temperature = data['main']['temp']

    humidity = data['main']['humidity']

    print("City:{}\t temperature:{}\t Humidity:{}".format(city_name, temperature, humidity))

if __name__ == '__main__':
    main()
