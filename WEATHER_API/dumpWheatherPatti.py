
# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules 
import requests, json, sys, time
from datetime import datetime
  
# Enter your API key here 
api_key = "795dd8f4c37a4ef6d3bde50bf367cfad"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = "Patti, IT"
#input("Enter city name : ") 
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 
  
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 

    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 

    w = x["wind"]
    wind_speed = w["speed"]
    wind_direction = 10
#    wind_direction = w["deg"]

    t = x["sys"]
    sunrise_time = t["sunrise"]
    sunset_time  = t["sunset"]
  
    # print following values 
    print(" Temperature (in Celsius unit) = " +
                    str(current_temperature-273.15) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n wind speed is = " +
                    str(wind_speed) + " m/s" +
          "\n wind direction is = " +
                    str(wind_direction) + " degrees north" +
          "\n description = " +
                    str(weather_description) +
          "\n sunrise time is = " +
                    datetime.utcfromtimestamp(int(sunrise_time)).strftime("%H:%M") +
          "\n sunset time is = " +
                    datetime.utcfromtimestamp(int(sunset_time)).strftime("%H:%M") )

    #fill new file only if request from API is succesfull
    if current_pressure>0:
        f = open("/home/pi/Documents/Python-Beginner-Pi-Projects/WEATHER_API/meteoPatti.txt", "w")
        f.write(
	        str(current_temperature-273.15) + "\n" +
        	str(current_pressure) + "\n" +
	        str(current_humidiy) + "\n" +
        	str(wind_speed) + "\n" +
	        str(wind_direction) + "\n" +
        	str(weather_description) + "\n" +
	        str(datetime.utcfromtimestamp(int(sunrise_time+7200)).strftime("%H:%M")) + "\n" +
	        str(datetime.utcfromtimestamp(int(sunset_time+7200)).strftime("%H:%M")) + "\n"
        )

        f.close()
  
else: 
    print(" City Not Found ") 

