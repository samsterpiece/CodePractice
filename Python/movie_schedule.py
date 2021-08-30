current_movies = {"The Grinch": "11:00am", 
"Rudolph": "1:00pm", "Frosty the Snowman": "3:00pm",
"Christmas Vacation": "5:00pm"}

print("We're showing the following movies: ")

#List all the current keys we have
for key in current_movies:
    print(key)

movie = input("What movie you would like the showtime for?\n")
showtime = current_movies.get(movie) #Grabs the values associated with the key

#If value doesn't match a key value, print movie isn't playing. Otherwise, print the showtime
if showtime == None:
    print("The requested movie isn't playing.")
else:
    print(movie, "is playing at: ", showtime)