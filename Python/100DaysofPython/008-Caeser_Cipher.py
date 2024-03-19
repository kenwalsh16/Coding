from caesar_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    final_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if direction == "encode":
                # Shift character and wrap around if it goes past 'z'
                new_index = (index + shift) % len(alphabet)
            elif direction == "decode":
                # Shift character back and wrap around if it goes past 'z'
                new_index = (index - shift) % len(alphabet)
            final_text += alphabet[new_index]
        else:
            # If character is not in alphabet, just append it as is
            final_text += char
    print(f"The {direction}d text is {final_text}")
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    
    input_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if input_continue == "no":
        should_continue = False
        print("Goodbye")
