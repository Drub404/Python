error_message = "This input is invalid."
options = ["A", "S", "D", "M"]

def main():
    choice = input("""
|===  Mr. Cat's Calculator        ===|
|===  Enter A for addition        ===|
|===  Enter S for substraction    ===|
|===  Enter D for division        ===|
|===  Enter M for multiplication  ===|
""")
    if choice in options:
        answer_function(choice)
    else:
        print(error_message)
        main()

def answer_function(choice):
    num1 = int(input("First number:"))
    num2 = int(input("Second number:"))
    if choice == "A":
        answer = num1 + num2
        print(answer)
    elif choice == "S":
        answer = num1 - num2
        print(answer)
    elif choice == "D":
        answer = num1 / num2
        print(answer)
    elif choice == "M":
        answer = num1 * num2
        print(answer)
    else:
        print(error_message)

main()