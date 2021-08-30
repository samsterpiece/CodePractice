menus = [["Egg Sandwich", "Bagel", "Coffee"],
["BLT", "PB&J", "Turkey Sandwich"], ["Soup", "Salad", "Spaghetti", "Taco"]]


print("Breakfast Menu:\t", menus[0]) #1st list
print("Lunch Menu:\t", menus[1]) #2nd list
print("Dinner Menu:\t", menus[2]) #3rd list

print("\nFood is: ", menus[0][1]) #Bagel

# #Another way- Dictionary of lists
menus = {
"\nBreakfast": ["Egg Sandwich", "Bagel", "Coffee"],
"Lunch": ["BLT", "PB&J", "Turkey Sandwich"],
"Dinner": ["Soup", "Salad", "Spaghetti", "Taco"]
}

# print("Breakfast Menu:\t", menus["Breakfast"])
# print("Lunch Menu:\t", menus["Lunch"])
# print("Dinner Menu:\t", menus["Dinner"])
 
 #Loop has access to both key and value
 #name is key, menu is value
for name, menu in menus.items():
    print(name, ":", menu)
