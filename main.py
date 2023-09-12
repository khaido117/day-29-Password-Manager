from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website_content = website_entry.get()
    password_content = password_entry.get()
    email_content = email_entry.get()

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

generate_password_button = Button(text="Generate Password", width=10)
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

