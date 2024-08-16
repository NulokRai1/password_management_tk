from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [choice(letters) for char in range(randint(8, 10))]
    password_list2 = [choice(symbols) for char in range(randint(2, 4))]
    password_list3 = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_list1 + password_list2 + password_list3

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            try:
                with open("management.json", mode="r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("management.json", mode="w") as file1:
                    json.dump(new_data, file1, indent=4)

            else:
                data.update(new_data)
                with open("management.json", mode="w") as file1:
                    json.dump(data, file1, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------------- Find Password -------------#

def find_password():
    website = website_entry.get()
    with open("management.json", "r") as data_file:
        data = json.load(data_file)
        try:
            p_data = data[website]
        except KeyError:
            messagebox.askokcancel(title="Error", message="No details for the website exists")
            website_entry.delete(0, END)

        else:
            email = p_data["email"]
            password = p_data["password"]
            messagebox.askokcancel(title=website, message=f"Email: {email}\n"
                                                              f"Password: {password}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
image = canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# label
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# entry
website_entry = Entry(width=21)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "nuloksampang@gmail.com")
password_entry = Entry(width=21)

# button
generate_button = Button(text="Generate Password", command=password_generator)
add_button = Button(text="Add", width=35, command=save)
search_button = Button(text="Search", command=find_password, width=13)

# grid l
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
# e
website_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
# b
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)

window.mainloop()
