#!/usr/bin/python
from rand import *
from menu import *


# dict of number of words corresponding to need dice rolls
rolldict = {'1': 5,'2': 10, '3': 15, '4': 20,'5': 25, '6': 30,'7': 35,
            '8': 40, '9': 45,'10': 50}

"""  Runs program  """

# choice of number of words to be generated
uservalue = menu_choice(rolldict)

# generates passpharse based on number of rolls that
rolled_dice = pharse_roll(uservalue)

# will print the dice numbers rolled to be used for the passpharse
print_dice_roll(rolled_dice)

# prints passpharse
print_passphare(passpharse)

# choice of adding random characters to passpharse
generate_rand_char()
