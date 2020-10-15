import time

error_message = "Your input was not valid."

while True:
    name = str(input("What's your name?"))
    navigation = input("""Hello {0}. 
    Enter [L] to log another time you smoked
    Enter [T] to see how many times you smoked already.
    Enter [R] to remove a log you've entered.
    [L/T/R]:""".format(name))

    if navigation == "L":
        print("L")
    elif navigation == "T":
        print("T")
    elif navigation == "R":
        print("R")
    else:
        print(error_message)
