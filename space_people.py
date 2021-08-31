#Retrieves data from internet, lists current people in space
#Http Request to web server
import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json() #Decode the JSON from the response

#print(json) #Print the json data

#Only have astronaut's name printed
print("The people currently in space are:")

for person in json['people']:
    print(person['name'])
