#Requests weather data from the weather API, parses the JSON, then prints weather
#values to the screen

import requests

api_key = 'de872ce5d28d450bb9d791318be16ca8'
city = 'Orlando'
url = "http://api.openweathermap.org/data/2.5/weather?q=" +city +"&appid=" + api_key + "&units=imperial"

request = requests.get(url)
json = request.json()


description = json.get("weather")[0].get("description")
print("Today's forecast is: ", description)

min_temp = json.get("main").get("temp_min")
print("Today's temperature min is: ", min_temp)

max_temp = json.get("main").get("temp_max")
print("Today's temperature max is: " , max_temp)