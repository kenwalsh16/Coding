# Password Generator
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
           "m", "n", "l", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G",
           "H", "I", "J", "K", "M", "N", "L", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")

num_chars = int(input("How many characters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

int_sum = num_numbers + num_symbols
password = []


for char in range(1, (num_chars - int_sum) + 1):
    password.append(random.choice(letters))
    
for num in range(1, num_numbers + 1):
    password.append(random.choice(numbers))
    
for symbol in range(1, num_symbols + 1):
    password.append(random.choice(symbols))

# Shuffle the combined list of characters
random.shuffle(password)

# Convert the list back to a string for the final password
password_final = ''.join(password)

# Print the final password
print(f"This is your new password: {password_final}")

