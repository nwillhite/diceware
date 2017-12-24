#!/usr/bin/python
import sys

def disclaimer():
    # print("\n" "Welcome to my implementation of diceware!!!! \n")
    print("\n", 30 * "*" , "DISCLAIMER" , 30 * "*", "\n")
    print("   This is not the most secure way of generating a password.")
    print("   Vist http://world.std.com/~reinhold/diceware.html")
    print("   Where there are instructions for the most secure and random passphrase.")
    print("\n", 30 * "*" , "DISCLAIMER" , 30 * "*", "\n")


def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print (" 1. Enter your own amount")
    print (" 2. 4 words")
    print (" 3. 5 Words")
    print (" 4. 6 Words")
    print (" 5. Look up values of manually rolled dice")
    print (" 6. Exit")
    print (67 * "-")


# menu for choosing amount of words
def menu_choice(rolldict):
    loop=True
    # prints disclaimer message
    disclaimer()
    while loop:         # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-6]: ")

        if choice == '1':
            print('How many words do you want in your passphrase?')
            choice = input("Enter your choice [1-20]: ")
            uservalue = int(choice) * 5
            break
        elif choice == '2':
            uservalue = rolldict['4']
            break
        elif choice == '3':
            uservalue = rolldict['5']
            break
        elif choice == '4':
            uservalue = rolldict['6']
            break
        elif choice == '5':
            print('Enter your results of manually rolling your dice')
            uservalue = input("Enter with spaces (ex: 12345 63421): ")
            break
        elif choice == '6':
            sys.exit()
        else:
            # Any integer inputs other than values 1-7 we print an error message
            print("Wrong option selection. Enter any key to try again..")

    return uservalue

# prompt for random character insert
def insert_char_menu():
    print('\nWould you like to insert a character at random?')
    loop = True
    while loop:
        choice = input("Enter your choice [y or n]: ")
        if choice ==  'y' or choice == 'Y':
            choice = input("How many characters? [1-10]: ")
            return int(choice)
        elif choice ==  'n' or choice == 'N':
            return 0


def print_dice_roll(dice):
    # used to print the numbers rolled that would represent words
    print("\n"+ "Your dice rolls: ", end="")
    for i in dice:
        print(i, " " , end="")


def print_passphrase(phrase):
    # prints out words based on the rolling of the dice
    print("\n"+ "Your passphrase is: ", end="")
    for i in phrase:
        print(i, "" , end="")
    print()
