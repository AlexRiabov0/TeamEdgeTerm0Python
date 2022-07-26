from gpiozero import LED
from time import sleep
myLed = LED(4)
BRate=0.25


def morse_dash():
    myLed.on()
    sleep(4*BRate)
    myLed.off()
    sleep(BRate)

def morse_pause():
    sleep(BRate)

def morse_dot():
    myLed.on()
    sleep(BRate)
    myLed.off()
    sleep(BRate)

CODE = {' ': '_', 
"'": '.----.', 
'(': '-.--.-', 
')': '-.--.-', 
',': '--..--', 
'-': '-....-', 
'.': '.-.-.-', 
'/': '-..-.', 
'0': '-----', 
'1': '.----', 
'2': '..---', 
'3': '...--', 
'4': '....-', 
'5': '.....', 
'6': '-....', 
'7': '--...', 
'8': '---..', 
'9': '----.', 
':': '---...', 
';': '-.-.-.', 
'?': '..--..', 
'A': '.-', 
'B': '-...', 
'C': '-.-.', 
'D': '-..', 
'E': '.', 
'F': '..-.', 
'G': '--.', 
'H': '....', 
'I': '..', 
'J': '.---', 
'K': '-.-', 
'L': '.-..', 
'M': '--', 
'N': '-.', 
'O': '---', 
'P': '.--.', 
'Q': '--.-', 
'R': '.-.', 
'S': '...', 
'T': '-', 
'U': '..-', 
'V': '...-', 
'W': '.--', 
'X': '-..-', 
'Y': '-.--', 
'Z': '--..', 
'_': '..--.-'}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence

while True:

    sentence = input("Enter sentence: ")
    encodedSentence = convertToMorseCode(sentence)
    print(encodedSentence)
    for i in encodedSentence:
        if i == ".":
            morse_dot()
        elif i == "-":
            morse_dash()
        else:
            morse_pause()