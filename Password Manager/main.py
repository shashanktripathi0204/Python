from tkinter import *
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
# ------------------------ PASSWORD GENERATOR -------------------------- #

# --------------------------- SAVE PASSWORD ---------------------------- #
def save():
    website = website_entry.get()
    domain = domain_entry.get()
    password = password_entry.get()

    if(len(website) == 0 or len(domain) == 0 or len(password) == 0):
        messagebox.showinfo(title="Oops", message="Madetory Fields are emmpty")
    else:
        # Pop up
        is_ok = messagebox.askokcancel(title = website, message = f"Entered Details: \nEmail : {domain}" 
                                                                  f"\nPassword : {password} \nIs it okay to save?")
        if is_ok:
            print("uwuwu")
            with open("./data.txt", mode='a') as file:
                # website | email/username | password
                file.write(f"{website} | {domain} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                domain_entry.delete(0, END)
                domain_entry.insert(0, "shashanktripathi99@outlook.com")




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
domain_entry.insert(0, "shashanktripathi99@outlook.com")



# Password Entries
password_entry = Entry(width=21)
# password_entry.insert(END, string="")
password_entry.grid(row = 3, column = 1,sticky="EW")



# Password Generate Button
generate_password_button = Button(text="Generate Password", width = 14)
generate_password_button.grid(row = 3, column = 2,sticky="EW")


# Add/Submit entries
submit_add = Button(text="Add", width=36, command = save)
submit_add.grid(row = 4, column = 1, columnspan = 2,sticky="EW")










window.mainloop()