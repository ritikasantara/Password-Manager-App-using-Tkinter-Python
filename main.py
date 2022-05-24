# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip
import json
from tkinter import messagebox


# Website and password search function

def search():
    try:
        with open("data.json", mode="r") as file:
            # reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("No Data File Found.")
    else:
        website = website_name_entry.get()
        if website in data:
            messagebox.showinfo(title="Website", message=f"Website: {website}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")

    finally:
        file.close()


# Password creation

def generate_password():
    from random import choice, randint, shuffle

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for char in range(randint(8, 10))]
    symbols_list = [choice(symbols) for char in range(randint(2, 4))]
    numbers_list = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #



def save_password():
    website = website_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="One or more fields empty", message="Please make sure you haven't left fields empty.")
    else:

        proceed = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail : "
                                                                f"{email}\n Password : {password}\nIs it ok to save?")

        if proceed:
            try:
                with open("data.json", mode="r") as file:
                    # reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)

            else:
                # updating old data with new data:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    # saving updated data
                    json.dump(data, file, indent=4)
            finally:
                website_name_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

password_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_name_entry = Entry(width=32)
website_name_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_name_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "ritikasantara@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="ew")

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
