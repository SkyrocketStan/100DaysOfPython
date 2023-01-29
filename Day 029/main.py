from tkinter import *
from tkinter import messagebox

import password_generator


# PASSWORD GENERATOR
def generate_password():
    password = password_generator.pass_gen()
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# SAVE PASSWORD
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showwarning(message="Do not leave empty fields")
        return

    is_ok = messagebox.askokcancel(title=website,
                                   message=f"Confirm your "
                                           f"entry\n"
                                           f"Email: {email}\n"
                                           f"Password: {password}")
    if is_ok:
        with open("password_unsafe.txt", mode="a") as file:
            file.write(f"{website}, {email}, {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# UI SETUP
window = Tk()
window.title("Password manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abuse@udemy.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
