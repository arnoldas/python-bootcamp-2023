import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

DATA_FILE = "data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(tkinter.END, password)
    pyperclip.copy(password)  # Copying password to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open(DATA_FILE, mode="r") as data_file:
                data = json.load(data_file)  # Reading old JSON data
        except FileNotFoundError:
            data = new_data  # Assigning new data
        else:
            data.update(new_data)  # Updating old data with new data
        finally:
            with open(DATA_FILE, mode="w") as data_file:
                json.dump(data, data_file, indent=4)  # Save JSON data [indent is used for better readability]
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
                website_entry.focus()


# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search_credentials():
    website = website_entry.get()
    try:
        with open(DATA_FILE, mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for '{website}' exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()  # Move the cursor to this entry when app is started

search_button = tkinter.Button(text="Search", command=search_credentials)
search_button.grid(row=1, column=2, sticky="EW")

name_label = tkinter.Label(text="Email/Username:")
name_label.grid(row=2, column=0)

email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(tkinter.END, "arnoldas@email.com")  # Fill default email

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = tkinter.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()

