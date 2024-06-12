# <abc Crea 2021> - <Oscar Eduardo Ochoa Velasco>

import sys

menu = """
1.- AlphaNumeric -> Morse Code
2.- Morse Code -> AlphaNumeric
0.- Exit
"""

#Creating the Dictionary for Alphanumeric and Morse relation
dic_Morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..'}

#Alphanumeric to Morse Function
def AlphaToMorse():
    print("AlphaNumeric -> Morse Code: ")
    text = input()
    for i in range(len(text)): #Search bucle                
        if text[i] == ' ': #Check for a space
            print("/ ", end = "")
        elif dic_Morse.get(text[i].upper()) != None: #Convert to upper for compare the same dictionary keys
            print(dic_Morse[text[i].upper()], end = " ") #Printing the correct Morse signal                
    print(end = "\n")    

#Morse to Alphanumeric Function
def MorseToAlpha():
    print("Morse Code -> AlphaNumeric: ")
    val = input()   
    indicator = 0
    for i in range(len(val)): #Search bucle
        if val[i] == ' ': #Check for a space
            for key, value in dic_Morse.items(): #Count the number of characters for know if its a single value
                if val[indicator:i] == value:
                    print(key, end = "")
                    indicator = i + 1
        elif val[i] == '/': #Check if have a slash that means a separated word
            indicator = i + 2 
            print(end = " ")
        elif (i + 1) == len(val): #Compare the values with a dictionary ID
            for key, value in dic_Morse.items():
                if val[indicator:i+1] == value:
                    print(key, end = "")
    print(end = "\n")   

while True:
    print(menu)
    try:
        opc = int(input())
        if opc == 1:
            AlphaToMorse()
        elif opc == 2:
            MorseToAlpha()
        elif opc == 0:
            sys.exit() #Close the program
    except ValueError: #Validate the user input
        print("ERROR!! Enter only a valid option")
