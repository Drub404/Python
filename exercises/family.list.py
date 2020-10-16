family1 = {
    "Dad": "John",
    "Mom": "Sophie",
    "Son": "Tom",
    "Daughter": "Laura",
}

def choiceoffamily():
    user_choice = str(input("""
    For what family member would you like more info about?:
    Dad, Mom, Son or Daughter?
    """))
    if user_choice in family1:
        if user_choice == "Dad":
            print(family1.get("Dad"))
        elif user_choice == "Mom":
            print(family1.get("Mom"))
        elif user_choice == "Son":
            print(family1.get("Son"))
        elif user_choice == "Daughter":
            print(family1.get("Daughter"))
    else:
        print("There was an error trying to execute this.")
        choiceoffamily()

choiceoffamily()