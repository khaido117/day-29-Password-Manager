from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip 
import json

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
    new_data = {
         website_content: {
              "email": email_content,
              "password": password_content,
         }
    }

    if len(website_content) == 0 or len(password_content) == 0:
            messagebox.showinfo(title="Oops!", message="Please enter information to continue.")
    else:
        try:
            with open("password.json", mode= "r") as file:
                #Reading old data 
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                #Saving updated data 
                json.dump(new_data, file, indent= 4)
        else:
            #Update old data with new data 
            data.update(new_data)
            with open("data.json", mode= "w") as file:
                json.dump(data, file, indent= 4)
                
        finally:
            clear_content()

def clear_content():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError as error_message:
        messagebox.showinfo(title="Error", message= f"{error_message}")

    else:
        if website in data: 
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message= f"Email: {email}, Password: {password}")
        else:
            messagebox.showinfo(title=website, message= "No data found")        

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

generate_password_button = Button(text="Generate Password", width=12, command=generate_password)
generate_password_button.grid(column=2, row= 3)

search_button = Button(text="Search",width=12, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add",width=42,command=lambda:[save_info(), clear_content()])
add_button.grid(column=1, row= 4,columnspan=2)

#Entries
website_entry = Entry(width=25)
website_entry.grid(column=1, row = 1)
website_entry.focus()

email_entry = Entry(width=42)
email_entry.grid(column=1, row = 2, columnspan=2)
email_entry.insert(0, "khai@gmail.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row = 3, columnspan=1)

window.mainloop()

