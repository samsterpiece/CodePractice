#Conditional statements on to stay inside or go outside depending on temperature

#Using or operator
temperature1 = 75
if temperature1 > 80 or temperature1 < 60:
    print("Stay Inside!")
else:
    print("Enjoy the outdoors!")

#Using and operator
temperature2 = 75
forecast = "sunny"
if temperature2 < 80 and forecast != "rain":
    print("Go outside!")
else:
    print("Stay inside!")

#Using not operator
forecast2 = "sunny"
#Make statement more readable
if not forecast2 == "rain":
    print("Go outside!")
else:
    print("Stay inside!")

#boolean
raining = True
if raining:
    print("Stay inside!")

if not raining:
    print("Go outside!")
else:
    print("Stay Inside!")


