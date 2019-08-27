#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 # prints "Greetings" to the console
colors = ['red','orange','yellow','green','blue','violet','purple'] # establishes a list of colors to be used in the program
play_again = ''                     # establishes a string determining whether or not the user wishes to play again
best_count = sys.maxsize            # a variable for storing the lowest number of guesses that lead to a win state
while (play_again != 'n' and play_again != 'no'):    # loops the code while the user wants to play again
    match_color = random.choice(colors) # chooses a random color from the colors list and stores it in match_color            
    count = 0                       # establishes a counter for the number of guesses
    color = ''                      # establishes a variable to store the guess of the player
    while (color != match_color):   # loops the following code while the user has not successfully guessed the match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line. sets the color to the user input
        color = color.lower().strip()   # removes any leading or trailing white space and makes the guess lowercase
        count += 1                  # increments the count by one
        if (color == match_color):  # if the color matches match_color, the following code will run
            print('Correct!')       # prints "Correct!" to the console
        else:                       # if the previous if statement was not true, this code will run
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))  # returns a try again statement, along with how many guesses the player has done so far
    print('\nYou guessed it in {0} tries!'.format(count))   # once the color matches the match color, the code will write how many times the player guessed to the console
    if (count < best_count):        # if the number of guesses is less than the lowest record, a new record is established and the player is let known
        print('This was your best guess so far!') # prints a congratluatory message
        best_count = count          # sets the best_count value to the new best
    play_again = input("\nWould you like to play again? ").lower().strip() # sets play_again to the player's input
print('Thanks for playing!')        # displays a goodbye message