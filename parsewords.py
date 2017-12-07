#!/usr/bin/python
import os
import sys
import re

dict = {}

def wordlist():
    with open("dicewarewords.txt") as file:
       for line in file:
          (key, val) = line.split()
          dict[int(key)] = val

    return dict
