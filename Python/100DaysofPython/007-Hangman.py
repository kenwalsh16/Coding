import random
from clear_screen import clear
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
print("Welcome to Hangman!")

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
player_lives = 6
end_of_game = False

# Use a list for the display word
display_word = ["_" for _ in range(chosen_word_length)]

# Print the initial display word
print(" ".join(display_word))

while not end_of_game:

    guess = input("\nGuess a letter: ").lower()
    
    clear()

    if guess in display_word:
        print(f"You've already guessed {guess}")
        
    # Check the guessed letter
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display_word[i] = guess
    if guess not in chosen_word:
        player_lives -= 1
        if player_lives == 0:
            end_of_game = True
            print("\nYou lose.")
            print("The word was: ", chosen_word)
        
    # Join the list back into a string and print
    print(f'{" ".join(display_word)}')

    if "_" not in display_word:
        end_of_game = True
        print("\nYou win!")
        
    # Print the stages
    print(stages[player_lives])