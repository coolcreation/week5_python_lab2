#!/usr/bin/env python3
# Jeff Bohn
# SWDV-210 Week_5 Lab_2
# 9/19/2024
# paragraph_to_list.py


################# Exercise 10-2 #################


def convertToList(filename):
    with open(filename) as file:
         text = file.read()    

    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.lower()
    
    words = text.split(" ")  
    return words



