#Requests weather data from the weather API, parses the JSON, then prints weather
#values to the screen

import requests

def get_weather_desc_and_temp():
    
    api_key = 'de872ce5d28d450bb9d791318be16ca8'
    city = 'Orlando'
    url = "http://api.openweathermap.org/data/2.5/weather?q=" +city +"&appid=" + api_key + "&units=imperial"

    request = requests.get(url)
    json = request.json()


    description = json.get("weather")[0].get("description")
    min_temp = json.get("main").get("temp_min")
    max_temp = json.get("main").get("temp_max")
    
    return {'description': description,
            'temp_min': min_temp,
            'temp_max': max_temp
            }

def main():
    #Print the results
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is: ", weather_dict.get('description'))
    print("Today's temperature min is: ", weather_dict.get('temp_min'))
    print("Today's temperature max is: " , weather_dict.get('temp_max'))
    
main()