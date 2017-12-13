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
    print (" 1. 1 Word")
    print (" 2. 2 Words")
    print (" 3. 3 Words")
    print (" 4. 4 Words")
    print (" 5. 5 Words")
    print (" 6. 6 Words")
    print (" 7. 7 Words")
    print (" 8. 8 Words")
    print (" 9. 9 Words")
    print (" 10. 10 Words")
    print (" 11. Exit")
    print (67 * "-")

def menu_choice(rolldict):
    loop=True

    while loop:         ## While loop which will keep going until loop = False
        print_menu()    ## Displays menu
        choice = input("Enter your choice [1-11]: ")

        if choice == '1':
            uservalue = rolldict['1']
            break
        elif choice =='2':
            uservalue = rolldict['2']
            break
        elif choice == '3':
            uservalue = rolldict['3']
            break
        elif choice == '4':
            uservalue = rolldict['4']
            break
        elif choice == '5':
            uservalue = rolldict['5']
            break
        elif choice == '6':
            uservalue = rolldict['6']
            break
        elif choice == '7':
            uservalue = rolldict['7']
            break
        elif choice == '8':
            uservalue = rolldict['8']
            break
        elif choice == '9':
            uservalue = rolldict['9']
            break
        elif choice == '10':
            uservalue = rolldict['10']
            break
            loop=False # This will make the while loop to end as not value of loop is set to False
        elif choice == '11':
            sys.exit()
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

    return uservalue
