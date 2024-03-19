# Simple Adventure game using conditionals and loops
# Welcome Message
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the Adventure Game!")
print("Your mission is to find the treasure.")
# Ask user for input
direction = input("You are at a t-junction road. Where do you want to go (left, right, or back)? Type 'l', 'r' or 'b'\n").lower()

# Conditional statement
if direction == "l":
    print("You went left, walk 5 miles and now you are at a lake.")
    print("There is an island in the middle of the lake.")
    # Ask user for input
    choice = input("Type 'w' to wait for a boat or 's' to swim across.\n").lower()

    # Conditional statement
    if choice == "w":
        print("You wasted 24 hours waiting for a boat, it delivers you to the island.")
        print("You see a house with 3 doors.")
        print("One red, one yellow, and one blue. Type 'r', 'y', or 'b' to choose a door.\n")
        # Ask user for input
        color = input("Which color do you choose?").lower()

        # Conditional statement
        if color == "r":
            print("You are immolated by a fire-thrower. Game Over.")
        elif color == "y":
            print("You found the treasure! You Win!")
        elif color == "b":
            print("You are eaten by beasts. Game Over.")
        else:
            print("You are a moron and are killed to prevent you from breeding. Game Over.")
    else:
        print("You chose to swim and are attacked by a trout. Game Over.")
        
elif direction == "r":
    print("You went right and were murdered by bandits. What pillock goes right? Game Over.")
else:
    print("You took the safe option, you pussy! You went back and are now at home. Game Over.")