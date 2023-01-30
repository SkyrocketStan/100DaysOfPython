import json
from tkinter import *
from tkinter import messagebox

import password_generator

JSON_FILE = "password.json"


# PASSWORD GENERATOR
def generate_password():
    password = password_generator.pass_gen()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


def get_json_data() -> json:
    try:
        with open(JSON_FILE) as file:
            data: json = json.load(file)
    except FileNotFoundError:
        data = None
    return data


def write_json_file(data):
    with open(JSON_FILE, mode="w") as file:
        json.dump(data, file, indent=4)


# SAVE PASSWORD
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password, }}

    # check for empty fields
    if not website or not email or not password:
        messagebox.showwarning(message="Do not leave empty fields")
        return

    is_ok = messagebox.askokcancel(title=website,
                                   message=f"Confirm your "
                                           f"entry\n"
                                           f"Email: {email}\n"
                                           f"Password: {password}")
    if is_ok:
        data: json = get_json_data()
        # Check for null data
        if data is None:
            data = new_data

        data.update(new_data)
        write_json_file(data)

        # clear fields in form
        website_entry.delete(0, END)
        password_entry.delete(0, END)


def search_password():
    website = website_entry.get()
    data = get_json_data()

    # Null check
    if data is None or website not in data:
        messagebox.showerror(title="Search result",
                             message=f"Data not found.")
        return

    email = data[website]["email"]
    password = data[website]["password"]
    messagebox.showinfo(title=website,
                        message=f"Email: {email}\nPassword: {password}")


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

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abuse@udemy.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()
