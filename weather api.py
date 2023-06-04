#Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

# Importing the requests library
import requests
import json
import sys

# api-endpoint
# URL = "http://api.openweathermap.org/data/2.5/weather?"

# # location given here
# location = sys.argv[1]

# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'q':location, 'appid':'b1b15e88fa797225412429c1c50c122a1'}

# # sending get request and saving the response as response object
# r = requests.get(url = URL, params = PARAMS)

# # extracting data in json format
# data = r.json()

# # extracting temperature, humidity, pressure and description
# temp = data['main']['temp']
# humidity = data['main']['humidity']
# pressure = data['main']['pressure']
# description = data['weather'][0]['description']

# # printing the output
# print("Temperature (in kelvin unit) = " +   str(temp) + 
#         "\nHumidity (in percentage) = " + str(humidity) +
#         "\nAtmospheric pressure (in hPa unit) = " + str(pressure) +
#         "\nDescription = " + str(description))

#convert above logic to function
def weather(location):
    URL = "http://api.openweathermap.org/data/2.5/weather?"
    PARAMS = {'q':location, 'appid':'b1b15e88fa797225412429c1c50c122a1'}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    try:
        data['main']['temp']
    except:
        print("Please enter a valid city name")
        return
    if data['cod'] == 401:
        print("Please enter a valid city name")
        return
    if data['cod'] == 404:
        print("Please enter a valid city name")
        return
    if data['cod'] == 429:
        print("Please enter a valid city name")
        return
    if data['cod'] == 500:
        print("Please enter a valid city name")
        return
    if data['cod'] == 503:
        print("Please enter a valid city name")
        return
    if data['cod'] == 504:
        print("Please enter a valid city name")
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
location = sys.argv[1]
location=input("Enter the city name: ")
try:
    weather(location)
except:

    print("Please enter a valid city name")
