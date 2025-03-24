from random import *
from string import *
from pyperclip import copy

def main():
    while True:
        try:
            length = int(input("How long should the password be? "))
            if length > 64 or length < 6:
                continue
            break
        except ValueError:
            continue

    lowercase_char = input("Should the password contain lowercase characters? (abcde) ").lower()
    uppercase_char = input("Should the password contain uppercase characters? (ABCDE) ").lower()
    symbol = input("Should the password contain symbols? (!@#$%) ").lower()
    number = input("Should the password contain numbers? (12345) ").lower()

    if lowercase_char not in ["y", "yes"] and uppercase_char not in ["y", "yes"] and symbol not in ["y", "yes"] and number not in ["y", "yes"]:
        print("You must select at least 1 password option!") 
        return

    pwd = generate_pwd(length, lowercase_char, uppercase_char, symbol, number)
    print(pwd)
    copy(pwd)
    print("Password copied to clipboard.")

    while True:
        answer = input("Do you want to generate another password with the same options? ").lower()
        if answer in ["y", "yes"]:
            print(generate_pwd(length, lowercase_char, uppercase_char, symbol, number))
            continue
        break

def generate_pwd(length, lowercase_char, uppercase_char, symbol, number):
    characters = ""
    if lowercase_char in ["y", "yes"]:
        characters += ascii_lowercase
    if uppercase_char in ["y", "yes"]:
        characters += ascii_uppercase
    if symbol in ["y", "yes"]:
        characters += punctuation
    if number in ["y", "yes"]:
        characters += digits

    pwd = ""
    while length > 0:
        pwd += choice(characters)
        length -= 1
    
    return pwd

main()