import random

def roll_dice():
    dicetotal = random.randint(1,6) + random.randint(1,6)
    return dicetotal

def main():
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        print(player1, " has won against", player2)
    elif roll2 > roll1:
        print(player2, " has won against", player1)
    else:
        print("You tie!")

main()