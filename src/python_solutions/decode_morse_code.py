letter_to_morse = {
    "A" : ".-",     "B" : "-...",     "C" : "-.-.",
    "D" : "-..",    "E" : ".",        "F" : "..-.",
    "G" : "--.",    "H" : "....",     "I" : "..",
    "J" : ".---",   "K" : "-.-",      "L" : ".-..",
    "M" : "--",     "N" : "-.",       "O" : "---",
    "P" : ".--.",   "Q" : "--.-",     "R" : ".-.",
    "S" : "...",    "T" : "-",        "U" : "..-",
    "V" : "...-",   "W" : ".--",      "X" : "-..-",
    "Y" : "-.--",   "Z" : "--..",     " " : "",
    "0" : "-----",  "1" : ".----",     "2" : "..---",
    "3" : "...--",  "4" : "....-",     "5" : ".....",
    "6" : "-....",  "7" : "--...",     "8" : "---..",
    "9" : "----.",  "SOS": "...---...", "!" : "-.-.--",
    "." : ".-.-.-"
}

def decodeMorse(morseCode):
    i = 1
    morseCode1 = morseCode
    while i == 1:
        if "   " in morseCode1:
            morseCode1 = morseCode1.replace("   ", "  ")
        else:
            i = 0
    split = morseCode1.split(' ')
    morse_to_letter = {morse: letter for letter, morse in letter_to_morse.items()}
    result =  ''.join(morse_to_letter[code] for code in split)
    while result[0] == " ":
        result = result[1:]
    while result[-1] == " ":
        result = result[:-1]
    return result


# -.-.--
print("|%s|" % decodeMorse('        ... --- ... -.-.--    - .... .      --.- ..- .. -.-. -.-      -... .-. --- .-- -.      ..-. --- -..-      .--- ..- -- .--. ...      --- ...- . .-.      - .... .      .-.. .- --.. -.--      -.. --- --. .-.-.-           '))
print(decodeMorse('.  .     . ... ..       .   .  . .  . . . .   . .    .   . .  .  .   .   '))
print(decodeMorse('.-- .... . .-. .      .- .-. .      -.-- --- ..-      - .... . .-. .      .. ...      -. ---      ... ..- -.-. ....      ..... ..... ...-- ....- .....      ....- ...-- .....      ----. ---.. .....      ----. ...-- ..... ....- ----. -----      ---.. ...-- ....-'))
print(decodeMorse('.  --.-    . .--- ---    . ...---...    '))
print(decodeMorse('.      .      .'))
print(decodeMorse('.... . -.--   .--- ..- -.. .'))
#------------------------------------------------------------------
# print decodeMorse('.... . .-.. .-.. ---      - .... . .-. .')

# def encodeMorse(text):
#     return ' '.join(letter_to_morse[letter] for letter in text)
#
# print encodeMorse('E     E     E')
# print encodeMorse('E   E   E')
