import random
import string 

def generate_password(min_length, has_numbers=True, has_special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    characters = letters
    if has_numbers:
        characters += digits 
    if has_special_characters:
        characters += special_characters


    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special_characters = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special_characters:
            has_special_characters = True

        meets_criteria = True
        if has_numbers:
            meets_criteria = meets_criteria and has_numbers
        if has_special_characters:
            meets_criteria = meets_criteria and has_special_characters

    return pwd

min_length = int(input("Enter the minimum length: "))
has_numbers = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special_characters = input("Do you want to have special characters (y/n)? ").lower() == "y"

pwd = generate_password(min_length, has_numbers, has_special_characters)

print("The generated password is:", pwd)
