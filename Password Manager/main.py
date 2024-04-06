from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
# ------------------------ PASSWORD GENERATOR -------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# --------------------------- SAVE PASSWORD ---------------------------- #
def save():
    website = website_entry.get()
    domain = domain_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email" : domain,
            "password" : password
        }
    }

    if(len(website) == 0 or len(domain) == 0 or len(password) == 0):
        messagebox.showinfo(title="Oops", message="Madetory Fields are emmpty")
    else:
        with open("./data.json", mode='r') as data_file:
            # Reading the old data
            data = json.load(data_file)
            # Updating the old data
            data.update(new_data)
        with open("./data.json", mode = "w") as data_file:
            # Saving the updated data
            json.dump(data, data_file, indent = 4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            domain_entry.delete(0, END)
            domain_entry.insert(0, "dummy@email.com")




# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 200, height = 200, highlightthickness=0)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

# website Label
website_label = Label(text = "Website:", font=(FONT_NAME,10,"bold"))
website_label.grid(row = 1, column = 0)

# Email/Username Label
email_username_label = Label(text = "Email/Username:", font=(FONT_NAME,10,"bold"))
email_username_label.grid(row = 2, column = 0)

# Password Label
password_label = Label(text = "Password:", font=(FONT_NAME,10,"bold"))
password_label.grid(row = 3, column = 0)

# Website Entries
website_entry = Entry(width=35)
# website_entry.insert(END, string="")
website_entry.grid(row = 1, column = 1, columnspan = 2,sticky="EW")
website_entry.focus()

# Email/Username(Domain) Entries
domain_entry = Entry(width=35)
# domain_entry.insert(END, string="")
domain_entry.grid(row = 2, column = 1, columnspan = 2,sticky="EW")
domain_entry.insert(0, "dummy@email.com")

# Password Entries
password_entry = Entry(width=21)
# password_entry.insert(END, string="")
password_entry.grid(row = 3, column = 1,sticky="EW")

# Password Generate Button
generate_password_button = Button(text="Generate Password", width = 14, command = generate_password)
generate_password_button.grid(row = 3, column = 2,sticky="EW")

# Add/Submit entries
submit_add = Button(text="Add", width=36, command = save)
submit_add.grid(row = 4, column = 1, columnspan = 2,sticky="EW")










window.mainloop()