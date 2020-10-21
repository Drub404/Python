def user_input():
    animal = str(input("What is your favorite animal?:"))
    number = int(input("What is your favorite number?:"))
    color = str(input("What is your favorite color?:"))
    madlibs_game(animal, number, color)

def madlibs_game(animal, number, color):
    if not all([animal, number, color]):
        print("You can't enter nothing as an answer.")
        user_input()
    else:
        print("You are a {0} that has {1} legs and has the color {2}.".format(animal, number, color))

user_input()