#!/usr/bin/python
import os
import random
from parsewords import wordlist
from menu import *

# dict for adding a random character into passpharse
randchar = {11: '~', 12: '!', 13: '#', 14: '$', 15: '%', 16: '^',
             21: '&', 22: '*', 23: '(', 24: ')', 25: '-', 26: '=',
             31: '+', 32: '[', 33: ']', 34: '_', 35: '{', 36: '}',
             41: ':', 42: ';', 43: '"', 44: ' ', 45: '<', 46: '>',
             51: '?', 52: '/', 53: '0', 54: '1', 55: '2', 56: '3',
             61: '4', 62: '5', 63: '6', 64: '7', 65: '8', 66: '9'}

# diceware wordlist
words = wordlist()

# passphrase holder
passphrase = []


def phrase_roll(num):
    currentstring = ""
    rolled_dice = []
    count = 0
    for x in range(0, num):
        # calls to get random roll
        currentstring+= str(roll_dice(6))

        # allows string length to get to five and then makes a new entry
        # into rolled_dice[].
        if (len(currentstring) % 5 == 0):
            rolled_dice.insert(count,int(currentstring))
            if int(currentstring) in words:
                passphrase.insert(count,words[int(currentstring)])
            count+=1
            currentstring= ""

    # will print the dice numbers rolled to be used for the passpharse
    print_dice_roll(rolled_dice)

    # prints passpharse
    print_passphrase(passphrase)


def roll_dice(size):
    # grabs random address for seed
    csprng = random.SystemRandom()
    # Random (probably large) integer
    diceroll = csprng.randint(0, sys.maxsize)
    # size used to restrict range of numbers generated
    diceroll = ((diceroll % size) + 1)
    return diceroll

def reroll(num):
    loop = True
    # loops until false
    while loop:
        print ("We you like to reroll? ")
        choice = input("Enter your choice [y or n]: ")

        if choice == 'y' or choice == 'Y':
            passphrase.clear()
            phrase_roll(num)

        elif choice == 'n' or choice == 'N':
            loop = False
        else:
            print("Wrong input choice...")


def insert_char(array):
    # grabs word to insert char
    word = roll_dice(len(array)-1)
    #print(word)
    # grabs a position in word to insert char
    position = roll_dice(len(array[word]))

    # generates the char to be inserted
    character = ''
    for i in range(0,2):
        character += str(roll_dice(6))
    # converts symbol to int for lookup
    character = int(character)
    # places random char from lookup into symbol
    character = randchar[character]

    s = array[word]
    new_word = s[:position-1] + character + s[position-1:]
    array[word] = new_word


def generate_rand_char():
    # choice of adding random characters to passphrase
    num_of_chars = insert_char_menu()

    # will generate amount of random characters user selects
    if (num_of_chars != 0):
        print_passphrase(passphrase)
        for i in range (0, num_of_chars):
            insert_char(passphrase)
        print_passphrase(passphrase)
        print()
    else:
        # prints passpharse
        print_passphrase(passphrase)
