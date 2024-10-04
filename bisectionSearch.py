"""
The program works as follows: 
you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
"""

low = 0
high = 100
guess = 0
print("Please think of a number between 0 and 100!")
while True:
    guess = (high+low)//2
    print("Is your secret number ", end=str(guess))
    print("?")
    command = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if command == 'c' or command == 'h' or command == 'l':
        if command == 'c':
            print('Game over. Your secret number was: ' + str(guess))
            break
        if command == 'h':
            high = guess
        if command == 'l':
            low = guess
    else:
        print('Sorry, I did not understand your input.')
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.
# Game over. Your secret number was: