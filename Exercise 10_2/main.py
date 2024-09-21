#!/usr/bin/env python3
# Jeff Bohn
# SWDV-210 Week_5 Lab_2
# 9/19/2024
# main.py


################# Exercise 10-2 #################

import paragraph_to_list as p


def getUniqueWords(words):
    my_set = set()  
    for i in words:
        my_set.add(i)
    
    my_list = [element for element in my_set]
    return my_list


def countSentences(filename):
    count = 0
    with open(filename) as file:
        text = file.read() 
    
    for i in text:
        if i == '.' or i == '?' or i == '!':
            count += 1
    return count


def main():
    filename = "gettysburg_address.txt"

    capital_words = "\nThe word counter program"
    print(capital_words.title())

    # count sentences
    sentences = countSentences(filename)
    print("\nSentences".ljust(30), sentences)

    # convert file to list
    words = p.convertToList(filename)
    print("Number of words".ljust(28), len(words))

    # sort list & return unique words
    unique_words = getUniqueWords(words)
    print("Number of unique words".ljust(28), len(unique_words))

    # unique word occurrences
    print(f"Unique word occurrences")
    for word in sorted(unique_words):
        print("".ljust(29) + word + " =" , words.count(word))


if __name__ == "__main__":
    main()

