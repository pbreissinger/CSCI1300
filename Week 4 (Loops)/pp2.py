'''
Peter Breissinger
pbreissinger@gmail.com
February 11, 2017
CSCI 1300
Judy Etchison
'''
from cs1gaphics import *
paper  = Canvas (500,500)

color1 = raw_input("Enter the color you want to use: ")

rows = raw_input("How many rows would you like to have? ")
if rows.isdigit():
    rows = int(rows)
else:
    num = 1

cols = raw_input("How many columns would you like to have? ")
if cols.isdigit():
    cols = int(cols)
else:
    cols = 1


    
