import winsound
import time 

## Challenge - The morse code encryption is to be hidden somewhere is the system linux file 

## Check GitHub ~ 

## ENCRYPTION - MORSE CODE 

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Morse Code encryption

message = "F  L A G"
message = message.upper()


def encrypt(message):
    encrypted = ''
    for character in message:
        if character != " ":
         encrypted += MORSE_CODE_DICT[character]
        else:
            encrypted += " "
    return encrypted

encrypt(message)

translated_MorseCode = encrypt(message)

## Further encrypting morse code by adding sound

for i in translated_MorseCode:
       if i == ".":
           winsound.PlaySound("dot", winsound.SND_FILENAME)
           time.sleep(0.1)
       elif i == "-":
           winsound.PlaySound("dash", winsound.SND_FILENAME)
           time.sleep(0.1)
       else:
           winsound.PlaySound("silent", winsound.SND_FILENAME)
           time.sleep(0.5) 

## DECRYPTION - MORSE CODE

"""

    small beep ---> dot 
    longer beep ---> dash 
    no beep / silent --> space 

    To find the morse code hear the sound and note all the details 

    the characters of a words are separated by space 

    note morse code for each character then write a python program to look for that program 

"""
array_Translated_Morse_code = translated_MorseCode.split(" ")
print(array_Translated_Morse_code)

decrypted = ''
for i in array_Translated_Morse_code:
   check = i
   for my_key, my_value in MORSE_CODE_DICT.items():
    if my_value == check:
       decrypted += my_key + " "
print(decrypted)