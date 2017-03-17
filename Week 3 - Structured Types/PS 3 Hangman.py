#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:12:02 2017

@author: keago
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
       if i not in lettersGuessed:
           return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    myString = ''
    for i in secretWord:
        if i in lettersGuessed:
            myString += i
        else:
            myString += '_ '
    return myString 


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    
    myString = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            myString += i
    return myString
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %s letters long." % len(secretWord))
    numGuesses = 8
    letters_Guessed = []
    availableLetters = getAvailableLetters(letters_Guessed)
    
    while True:
        print("-" * 10)
        if numGuesses == 0:
            print("Sorry, you have no more guesses. The word was " + secretWord + ".")
            return
            
        if isWordGuessed(secretWord, letters_Guessed):
            print("Congratulations, you won!")
            return
            
        print("You have %d guesses left" % numGuesses)
        print("Available letters: %s" % availableLetters)
        guess = str(input("Please guess a letter: ")).lower()
        
        if guess in letters_Guessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, letters_Guessed))
            continue
        
        letters_Guessed.append(guess)
        availableLetters = getAvailableLetters(letters_Guessed)
        if guess in secretWord:
            print("Good Guess: " + getGuessedWord(secretWord, letters_Guessed))
        
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, letters_Guessed))
            numGuesses -= 1





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
