error_message = "This input is invalid."

def main():
    choice = input("""
    Welcome to Mr. Cat's first calculator!

    Please enter your choice for the calculator.
    Addition/Substraction/Division/Multiplication
    A - S - D - M
    :""")

    if choice == "A":
        answer_function(choice)
    elif choice == "S":
        answer_function(choice)
    elif choice == "D":
        answer_function(choice)
    elif choice == "M":
        answer_function(choice)
    else:
        print(error_message)

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