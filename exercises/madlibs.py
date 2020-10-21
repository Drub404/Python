import time

def user_input():

    """
    Function called to start the game.
    Asks user input and then calls the madlibs_game function.
    """

    animal = input("What is your favorite animal?:")
    number = input("What is your favorite number?:")
    color = input("What is your favorite color?:")
    madlibs_game(animal, number, color)

def madlibs_game(animal, number, color):
    
    """
    Function that first checks if one of the user_input variables is None.
    If that's true, it'll restart the game with a message that they forgot
    a parameter. 

    Else it will generate a sentence with all the user's input.
    """
    
    if not all([animal, number, color]):
        print("Missing argument for 1 or more parameters.\nRestarting the game.")
        time.sleep(1)
        user_input()
    else:
        print("You are a {0} that has {1} legs and has the color {2}.".format(animal, number, color))

user_input()