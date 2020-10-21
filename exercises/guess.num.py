""" Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. 
Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced. 
The clue can be multiples, divisible, greater or smaller, or a combination of all.

You will also need functions to compare the inputted number with the guessed number, 
to compute the difference between the two, and to check whether an actual number was inputted or not in this python project.

https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/ """

import random
import sys
import time

score = 5

def start_game():
    print("""Welcome to Guess The Number!
        I have chosen a random number ranging from 1-10.
        Every time you guess wrong, your score gets reduced.
        If you're left with 0 score, the game will stop and output the number.""")
    num = random.randint(1, 100)
    guessing(num, score)

def guessing(num, score):
    if score <= 0:
        print("Unfortunately, you have no more tries left. The number was {0}".format(num))
        time.sleep(3)
        sys.exit
    else:
        guess = input("Guess the number:")
        compare_num(num, guess, score)
    
def compare_num(num, guess, score):
    if guess == "":
        print("You haven't entered anything.")
        guessing(num, score)
    elif guess != num:
        score -= 1
        print("Wrong guess.")
        guessing(num, score)
    else:
        print("You guessed the number right! You received {0} score.".format(score))
        again = str(input("Would you like to play again?:"))
        play_again(again)

def play_again(again):
    if again.lower() == "yes":
        start_game()
    elif again.lower() == "no":
        sys.exit("Thanks for playing me! Bye.")
    else:
        sys.exit("Invalid input.")

start_game()