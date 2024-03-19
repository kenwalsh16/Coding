# Rock, Paper, Scissors Game
import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_selection = int(input())

computer_selection = random.randint(0, 2)  # 0 = Rock, 1 = Paper, 2 = Scissors

if user_selection == 0:
    print("You chose Rock.")

    if computer_selection == 0:
        print("Computer chose Rock.")
        print("It's a draw.")
    elif computer_selection == 1:
        print("Computer chose Paper.")
        print("You lose.")
    else:
        print("Computer chose Scissors.")
        print("You win.")
        
elif user_selection == 1:
    print("You chose Paper.")

    if computer_selection == 0:
        print("Computer chose Rock.")
        print("You win.")
    elif computer_selection == 1:
        print("Computer chose Paper.")
        print("It's a draw.")
    else:
        print("Computer chose Scissors.")
        print("You lose.")
        
elif user_selection == 2:
    print("You chose Scissors.")

    if computer_selection == 0:
        print("Computer chose Rock.")
        print("You lose.")
    elif computer_selection == 1:
        print("Computer chose Paper.")
        print("You win.")
    else:
        print("Computer chose Scissors.")
        print("It's a draw.")

