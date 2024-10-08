# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/Dell/Documents/Personal/pytho/problemset3/words.txt"

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
    secretWordList = list(secretWord)
    count = 0
    for val in secretWordList:
        if val in lettersGuessed:
            count += 1

    if count == len(secretWordList):
        return True
    else:
        return False      



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE..
    guess = list("_"*len(secretWord))
    secretWordList = list(secretWord)
    count = 0
    for i in range(len(secretWordList)):
        if secretWordList[i] in lettersGuessed:
            guess[i] = secretWordList[i]
            
    return " ".join(guess)     



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = list(string.ascii_lowercase)
    result = []
    for i in range(len(letters)):
        if letters[i] not in lettersGuessed:
            result.append(letters[i])
    return "".join(result)
    

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
    totalLetters = len(secretWord)
    lettersGuessed = []
    i = 8
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(totalLetters) + " sletters long.")
    while i > 0:
        availableLen = getAvailableLetters(lettersGuessed)
        print("You have " + i +" guesses left.")
        print("Available letters: "+ availableLen)
        guess = input("Please guess a letter:")
        if len(lettersGuessed) == 0:
            lettersGuessed.append(guess)

        guessWord = getGuessedWord(lettersGuessed)
        if len(getAvailableLetters(lettersGuessed)) == availableLen :
            print("Oops! You've already guessed that letter: " + guessWord)
        else:
            print("Good guess: " + guessWord)






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)


secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))