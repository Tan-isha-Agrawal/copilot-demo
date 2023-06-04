#Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

# Importing the requests library
import requests
import json
import sys


#convert above logic to function
def weather(location):
    URL = "http://api.openweathermap.org/data/2.5/weather?"
    PARAMS = {'q':location, 'appid':'3921a6d2246b41b25bfc5a5a7458f9a7'}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    try:
        print(data['main']['temp'])
    except:
        print("Please enter a valid city name")
        return
    if data['cod'] == 401:
        print("enter a valid api key")
    if data['cod'] == 404:
        print("enter a valid city name")
        return
    if data['cod'] == 500:
        print("internal server error")
        return

       
    if data['cod'] == 200:
        
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        print("Temperature (in kelvin unit) = " +   str(temp) + 
            "\nHumidity (in percentage) = " + str(humidity) +
            "\nAtmospheric pressure (in hPa unit) = " + str(pressure) +
            "\nDescription = " + str(description))
# location = sys.argv[1]
location=input("Enter the city name: ")

weather(location)

#sample input: python weather api.py london
#sample input: python weather api.py london,uk
