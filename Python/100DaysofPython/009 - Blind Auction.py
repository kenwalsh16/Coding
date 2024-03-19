import os

# Function to clear the screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
        
from auction_art import logo
print(logo)
print("Welcome to the Secret Auction program.")

# Dictionary to store the bids
bids = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    
    continueAuction = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continueAuction == "yes":
        clear_screen()
    else:
        break

# Determining the highest bid outside the while loop
clear_screen()
highest_bid = 0
winner = ""
for bidder, bid_amount in bids.items():
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}.")
