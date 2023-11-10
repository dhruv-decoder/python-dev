# Define a dictionary for Morse code mappings
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' ', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '/': '-..-.', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', '(': '-.--.', ')': '-.--.-'
}


def text_to_morse(text):
    morse_code_text = ""
    for letter in text:
        if letter in morse_code_dict:
            morse_code_text += morse_code_dict[letter]
        else:
            morse_code_text += " "  # Handle unknown characters gracefully
    return morse_code_text


is_continue = True

while is_continue:
    text = input("Enter a string to get its Morse code: ").upper()

    try:
        morse_code_text = text_to_morse(text)
        print(f"Your Morse code for the given text is: {morse_code_text}")
    except KeyError:
        print("Error: Invalid character in input. Only letters, numbers, and common symbols are supported.")

    choice = input("Do you need the Morse code for another text? Type 'Y' for yes or 'N' for no: ").lower()

    if choice != 'y':
        is_continue = False

# End of the program
