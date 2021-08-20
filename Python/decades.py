#Simple program that calculates how many decades old one is after inputting age.

age = int(input("How old are you? "))
decadeCalculator = age // 10
years = age % 10
print("You are ", decadeCalculator, " decades and", years, " years old.")
