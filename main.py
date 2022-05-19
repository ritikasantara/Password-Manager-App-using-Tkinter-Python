# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

password_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200,  highlightthickness=0)
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

website_name_entry = Entry(width=43)
website_name_entry.grid(column=1, row=1, columnspan=2)
website_name_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ritikasantara@gmail.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()