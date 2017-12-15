#!/usr/bin/python
import os
import sys
import re

dict = {}

def wordlist():
    with open("beale.wordlist.txt") as file:
       for line in file:
          (key, val) = line.split()
          dict[int(key)] = val

    return dict
