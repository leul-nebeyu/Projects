from tkinter import *
from random import *
from string import *

root = Tk()
root.geometry('600x300')
root.title("Password Generator")

def main():
    length = int(lgth.get())
    lowercase_char = lower_char.get()
    uppercase_char = upper_char.get()
    symbol = smb.get()
    number = nb.get()

    characters = ""
    if lowercase_char:
        characters += ascii_lowercase
    if uppercase_char:
        characters += ascii_uppercase
    if symbol:
        characters += punctuation
    if number:
        characters += digits

    show_pwd_text = StringVar()
    show_pwd = Label(root, textvariable=show_pwd_text)
    show_pwd.grid(row=5, column=10, sticky="W")

    if characters == "":
        show_pwd_text.set("You must select at least 1 password option!")
    else:
        pwd = generate_pwd(length, characters)
        show_pwd_text.set(pwd)

def generate_pwd(length, characters):
    pwd = ""
    while length > 0:
        pwd += choice(characters)
        length -= 1
    
    return pwd

Label(root, text='Password Generator').grid(row=10, column = 150,sticky=W)
generate_bt = Button(root, text="Generate Password", command=main)
generate_bt.place(x=200, y=50)

lgth = Spinbox(root, from_ = 8, to = 64)
lgth.grid(row=5, sticky=W)
lower_char = IntVar()
Checkbutton(root, text='Lowercase Characters', variable=lower_char).grid(row=20, sticky=W)
upper_char = IntVar()
Checkbutton(root, text='Uppercase Characters', variable=upper_char).grid(row=25, sticky=W)
smb = IntVar()
Checkbutton(root, text='Symbols', variable=smb).grid(row=30, sticky=W)
nb = IntVar()
Checkbutton(root, text='Numbers', variable=nb).grid(row=35, sticky=W)

root.resizable(False, False)
root.mainloop()