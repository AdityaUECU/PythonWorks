import requests
import json
import pyttsx3

city = input("Enter the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=36cc585208d74a27bf6135633233107&q={city}"

r = requests.get(url)

weatherdic = json.loads(r.text)
temp = weatherdic["current"]["temp_c"]
w = weatherdic["current"]["condition"]["text"]
h = weatherdic["current"]["humidity"]
c = weatherdic["current"]["cloud"]

speak = pyttsx3.init()
speak.say(f"The current weather in {city} is {temp} degrees celsius and the condition is {w} and the humidity is {h} and the clouds are {c}")
print(f"The current weather in {city} is {temp} degrees celsius and the condition is {w} and the humidity is {h} and the clouds are {c}")
speak.runAndWait()

goodbye = pyttsx3.init()
goodbye.say("Thank you for visiting Aditya's Weather App")
goodbye.runAndWait()