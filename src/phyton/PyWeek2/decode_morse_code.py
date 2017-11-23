letter_to_morse = {
    "a" : ".-",     "b" : "-...",     "c" : "-.-.",
    "d" : "-..",    "e" : ".",        "f" : "..-.",
    "g" : "--.",    "h" : "....",     "i" : "..",
    "j" : ".---",   "k" : "-.-",      "l" : ".-..",
    "m" : "--",     "n" : "-.",       "o" : "---",
    "p" : ".--.",   "q" : "--.-",     "r" : ".-.",
    "s" : "...",    "t" : "-",        "u" : "..-",
    "v" : "...-",   "w" : ".--",      "x" : "-..-",
    "y" : "-.--",   "z" : "--..",     " " : "/"
}

def decodeMorse(morseCode):
    morse_to_letter = {morse: letter for letter, morse in letter_to_morse.items()}
    return ''.join(morse_to_letter[code] for code in morseCode.split())







#------------------------------------------------------------------
# print decodeMorse('.... . .-.. .-.. --- / - .... . .-. .')

# def encodeMorse(text):
#     return ' '.join(letter_to_morse[letter] for letter in text)
#
# print encodeMorse('hello there')
