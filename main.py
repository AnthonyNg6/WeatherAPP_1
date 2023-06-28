import requests
import tkinter as tk
import math

API_KEY = "3ace7596caad5c7cebbc0e883eeb0fef"

root = tk.Tk()

root.geometry("1280x720")
root.title("Weather App 1")
root.configure(background='light blue')

myentry = tk.Entry(root,width=20,font=('Helvetica',24))
city_name = myentry.get()
myentry.pack(padx=20,pady=50)

root.mainloop()

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()
    temp = response['main']['temp']
    temp = math.floor((temp - 273.15)*1.8)+32

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like - 273.15)*1.8)+32

    humidity = response['main']['humidity']

    print("Temperature: " + str(temp) + "°F")
    print("Feels like: " + str(feels_like) + "°F")
    print("Humidity: " + str(humidity) + "%")

get_weather(API_KEY,city_name)

