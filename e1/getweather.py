#!/usr/bin/python

# Author: Peter Straka

#Retrieves weather data from https://openweathermap.org/api
#l It uses the current weather data API: https://openweathermap.org/current
#l It uses pyown: https://pypi.python.org/pypi/pyowm
#l The python script uses no arguments, only the following environment variables:
#	OPENWEATHER_API_KEY
#	CITY_NAME
#l It outputs to stdout

# sudo pip install pyowm
#$ export
#declare -x OPENWEATHER_API_KEY="xxxxxxxxxxxx"
#declare -x CITY_NAME="Honolulu"
#$ python getweather.py
#source=openweathermap, city="Honolulu", description="few clouds", temp=70.2, humidity=75

# docker run --rm -e OPENWEATHER_API_KEY="xxx" -e CITY_NAME="Honolulu" weather:dev

import os
import pyowm

api_key = os.getenv('OPENWEATHER_API_KEY', 'xxxxxxxxxxxx')
owm = pyowm.OWM(api_key)  # You MUST provide a valid API key

# Search for current weather 
source = 'openweathermap'
city = os.getenv('CITY_NAME', 'Honolulu')
observation = owm.weather_at_place(city)
w = observation.get_weather()

# Weather details
#print('apikey: {}'.format(api_key))                  				
#print('city: {}'.format(city))                  				
#print('code: {}'.format(w.get_weather_code()))                  				
#print('status: {}'.format(w.get_status()))                  				
#print('wind: {}'.format(w.get_wind()))                  						
#print('humidity: {}'.format(w.get_humidity()))              			
#print('temperature: {}'.format(w.get_temperature('celsius'))) 

print('source={}, city="{}", description="{}", temp={}, humidity={} '.format(
	source, city, 
	w.get_status(),
	w.get_temperature('celsius')['temp'], 
	w.get_humidity()
	)) 
