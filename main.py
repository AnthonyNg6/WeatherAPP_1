import requests
import math
import customtkinter

API_KEY = "3ace7596caad5c7cebbc0e883eeb0fef"


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x700")
root.title("Weather App 1")
root.configure(background='light blue')


myentry = customtkinter.CTkEntry(root,width=350,justify='center',font=("Verdana",36))
myentry.pack(padx=20,pady=75)
city_name = myentry.get()


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

