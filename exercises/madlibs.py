""" The program design is such that it will ask users to enter a series of inputs that will be considered as a Mad Lib. 
Mad lib is one of the python projects for beginners. 

The input could be anything, an adjective, a noun, a pronoun, etc. 
Once all the inputs are entered, the application will take the data and arrange the inputs into a story template form. 
https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/ """

import time
import sys

def user_input():

    """ Function called to start the game.
    Asks user input and then calls the madlibs_game function. """

    animal = input("What is your favorite animal?:")
    number = input("What is your favorite number?:")
    color = input("What is your favorite color?:")
    madlibs_game(animal, number, color)

def madlibs_game(animal, number, color):
    
    """ Function that first checks if one of the user_input variables is None.
    If that's true, it'll restart the game with a message that they forgot
    a parameter. 

    Else it will generate a sentence with all the user's input. """
    
    if not all([animal, number, color]):
        print("Missing argument for 1 or more parameters.\nRestarting the game.")
        time.sleep(1)
        user_input()
    else:
        print("You are a {0} that has {1} legs and has the color {2}.".format(animal, number, color))
        again = str(input("Would you like to play again?:"))
        play_again(again)

def play_again(again):
    if again.lower() == "yes":
        user_input()
    elif again.lower() == "no":
        sys.exit("Thanks for playing me! Bye.")
    else:
        sys.exit("Invalid input.")

user_input()