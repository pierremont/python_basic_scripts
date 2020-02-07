#!/bin/python

import requests


response = requests.post("http://api.openweathermap.org/data/2.5/weather?q=Bucharest,ro&units=metric&lang=ro&APPID=your_key")
print (response.status_code)
print (response.text)

print()

#response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Bucharest,ro&units=metric&lang=ro&APPID=your_key")
#print (response.status_code)
#print (response.text)