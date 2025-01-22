print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You are at the crossroad, where do you want to go? '
                'Type "Left" or "Right".\n').lower()

if choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake.'
          ' Type "Wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors. One red, One yellow and One blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
           print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
           print("You found the treasure! You Win")
        elif choice3 == "blue":
           print("You enter a room of ghosts. Game Over.")
        else:
           print("You chose a door that doesn't exists. Game Over.")

    else:
        print("You got attacked by sharks and they had a nice feast because of you!. Game Over.")


else:
    print("You fell into a hole and broke your bones and died. Game Over.")
