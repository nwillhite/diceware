#!/usr/bin/python
import os
import sys
import random
from parsewords import wordlist
from menu import *

# users entered choice
uservalue = 0
# diceware wordlist
words = wordlist()
# dict of number of words corresponding to need dice rolls
rolldict = {'1': 5,'2': 10, '3': 15, '4': 20,'5': 25, '6': 30,'7': 35,
            '8': 40, '9': 45,'10': 50}
#dict for adding a random character into passpharse
randchar = {11: '~', 12: '!', 13: '#', 14: '$', 15: '%', 16: '^',
             21: '&', 22: '*', 23: '(', 24: ')', 25: '-', 26: '=',
             31: '+', 32: '[', 33: ']', 34: '_', 35: '{', 36: '}',
             41: ':', 42: ';', 43: '"', 44: ' ', 45: '<', 46: '>',
             51: '?', 52: '/', 53: '0', 54: '1', 55: '2', 56: '3',
             61: '4', 62: '5', 63: '6', 64: '7', 65: '8', 66: '9'}
# passpharse holder
passpharse = []

#if choice in wordvalue:
#    uservalue = wordvalue[choice]

disclaimer()
uservalue = menu_choice(rolldict)


"""
arr = [random.randint(0,sys.maxsize) for _ in range(5)]
for i in arr:
    print(i)
"""

def pharseroll(num):
    currentstring = ""
    rolled_dice = []
    count = 0
    for x in range(0, num):
        # calls to get random roll
        currentstring+= str(roll_dice(6))

        # allows string length to get to five and then makes a new entry
        # into rolls[].
        if (len(currentstring) % 5 == 0):
            rolled_dice.insert(count,int(currentstring))
            if int(currentstring) in words:
                passpharse.insert(count,words[int(currentstring)])
            count+=1
            currentstring= ""

    return rolled_dice


def roll_dice(size):
    # grabs random address for seed
    csprng = random.SystemRandom()
    # Random (probably large) integer
    diceroll = csprng.randint(0, sys.maxsize)
    diceroll = ((diceroll % size) + 1)
    return diceroll


def insert_char(array):
    # grabs word to insert char
    word = roll_dice(len(array)-1)
    #print(word)
    # grabs a position in word to insert char
    position = roll_dice(len(array[word]))

    symbol = ''
    # generates the char to be inserted
    for i in range(0,2):
        symbol += str(roll_dice(6))
    # converts symbol to int for lookup
    symbol = int(symbol)
    #places random char from lookup into symbol
    symbol = randchar[symbol]

    s = array[word]
    new_word = s[:position-1] + symbol + s[position-1:]
    array[word] = new_word
    #s[:4] + '-' + s[4:]


def print_passphare(dice, pharse):
    print("\n"+ "Your dice rolls: ", end="")
    for i in dice:
        print(i, " " , end="")

    print("\n"+ "Your passpharse is: ", end="")
    for i in pharse:
        print(i, " " , end="")
    print('\n')


rolled_dice = pharseroll(uservalue)
#insert_char(passpharse)
print_passphare(rolled_dice,passpharse)
