from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website_content = website_entry.get()
    password_content = password_entry.get()
    email_content = email_entry.get()

    if len(website_content) == 0 or len(password_content) == 0:
            messagebox.showinfo(title="Oops!", message="Please enter information to continue.")
    else: 

        is_ok = messagebox.askokcancel(title="website", message= f"Please confirm you info: \n Email: {email_content}\n Website: {website_content} \n Password: {password_content} \n Is it ok to save? ")

        if is_ok:
            with open("password.txt", mode= "a") as file:
                file.writelines(website_content + "|" + email_content + "|" + password_content + "\n")
    
def clear_content():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100 ,image = logo_img)
canvas.grid(column=1, row = 0)

#Labels 

website_label = Label(text= "Website: ")
website_label.grid(column=0, row= 1)

email_label = Label(text= "Email/Username: ")
email_label.grid(column=0, row= 2)

password_label = Label(text= "Password: ")
password_label.grid(column=0, row= 3)

#Buttons

generate_password_button = Button(text="Generate Password", width=10, command=generate_password)
generate_password_button.grid(column=2, row= 3)

add_button = Button(text="Add",width=36,command=lambda:[save_info(), clear_content()])
add_button.grid(column=1, row= 4,columnspan=2)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row = 1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row = 2, columnspan=2)
email_entry.insert(0, "khai@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row = 3, columnspan=1)

window.mainloop()

