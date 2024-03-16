#7. Write the Morse code translator. Write a function that takes as input a string (one word or a sentence) 
#and returns encoded string in the Morse code.

def morse_translator(text):
    morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    }
    translation = ""
    upper_words = text.upper()
    for letter in upper_words:
        code = morse_code_dict[letter]
        translation += code
    return translation
        
text = "sos"

print(morse_translator(text))


