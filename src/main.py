#!/usr/bin/python
from rand import *
from menu import *


# dict of number of words corresponding to need dice rolls
rolldict = {'1': 5,'2': 10, '3': 15, '4': 20,'5': 25, '6': 30,'7': 35,
            '8': 40, '9': 45,'10': 50}

"""  Runs program  """
# choice of number of words to be generated
uservalue = menu_choice(rolldict)

# generates passphrase based on number of rolls that
if type(uservalue).__name__ == 'int':
    phrase_roll(uservalue)
    reroll(uservalue)
elif type(uservalue).__name__ != 'int':
    split_input(uservalue)


# choice of adding random characters to passphrase
generate_rand_char()
