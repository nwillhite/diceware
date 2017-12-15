#!/usr/bin/python

def disclaimer():
    #print("\n" "Welcome to my implementation of diceware!!!! \n")
    print("\n", 30 * "*" , "DISCLAIMER" , 30 * "*", "\n")
    print("   This is not the most secure way of generating a password.")
    print("   Vist http://world.std.com/~reinhold/diceware.html")
    print("   Where there are instructions for the most secure and random passpharse.")
    print("\n", 30 * "*" , "DISCLAIMER" , 30 * "*", "\n")

def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print (" 1. Enter your own amount")
    print (" 2. 5 Words")
    print (" 3. 6 Words")
    print (" 4. 7 Words")
    print (" 5. 8 Words")
    print (" 6. 9 Words")
    print (" 7. Exit")
    print (67 * "-")

def print_menu1():
    print('How many words do you want in your passpharse?')
    choice = input("Enter your choice [1-20]: ")
    return choice

#menu for choosing amount of words
def menu_choice(rolldict):
    loop=True

    while loop:         ## While loop which will keep going until loop = False
        print_menu()    ## Displays menu
        choice = input("Enter your choice [1-11]: ")

        if choice == '1':
            print('How many words do you want in your passpharse?')
            choice = input("Enter your choice [1-20]: ")
            uservalue = int(choice) * 5
            break
        elif choice == '2':
            uservalue = rolldict['5']
            break
        elif choice == '3':
            uservalue = rolldict['6']
            break
        elif choice == '4':
            uservalue = rolldict['7']
            break
        elif choice == '5':
            uservalue = rolldict['8']
            break
        elif choice == '6':
            uservalue = rolldict['9']
            break
        elif choice == '7':
            sys.exit()
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

            #loop=False # This will make the while loop to end as not value of loop is set to False
    return uservalue


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

def print_passphare(pharse):
    # prints out words based on the rolling of the dice
    print("\n"+ "Your passpharse is: ", end="")
    for i in pharse:
        print(i, "" , end="")
    print()
