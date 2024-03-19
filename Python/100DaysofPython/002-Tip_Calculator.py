# Print a Welcome message
# Ask the user for the total bill
# Ask the user for the number of people to split the bill
# Ask the user for the percentage tip
# Calculate and print the tip amount

print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
tipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))
totalBill *= 1 + (tipPercent / 100)
billPerPerson = totalBill / numPeople
# Format the bill to 2 decimal places
final_amount = "{:.2f}".format(billPerPerson)
print(f"Each person should pay: ${final_amount}")