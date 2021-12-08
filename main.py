from tkinter import *
import json
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(4, 9))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 5))]
    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please check if you've entered all your information")
    else:
        try:
            with open("../password-manager/../../../Documents/data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("../password-manager/../../../Documents/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=5)
        else:
            data.update(new_data)
            with open("../password-manager/../../../Documents/data.json", "w") as data_file:
                json.dump(data, data_file, indent=5)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)

            website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open("../password-manager/../../../Documents/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    else:
        if website in data:
            email = data[website]["email"]
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Username: {username} \n Password: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {website} exits!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager GUI 🔐")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo_img.png").subsample(3, 3)
canvas.create_image(115, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website & Search Widgets
website_label = Label(text="Website Name:", font=("Ariel", 15))
website_label.grid(row=1, column=0)
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()
search_btn = Button(text="Search Website", command=find_password, fg="#516BEB")
search_btn.config(padx=5, pady=5)
search_btn.grid(row=1, column=2)

# Email Widgets
email_label = Label(text="Email:", font=("Ariel", 15))
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

# Username Widgets
username_label = Label(text="Username:", font=("Ariel", 15))
username_label.grid(row=3, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=3, column=1, columnspan=2)

# Password & Generate Widgets
password_label = Label(text="Password:", font=("Ariel", 15))
password_label.grid(row=4, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=4, column=1)
generate_btn = Button(text="Generate Password", command=generate_password, fg="#516BEB")
generate_btn.grid(row=4, column=2)
generate_btn.config(padx=3, pady=3)

# Add info Widgets
add_btn = Button(text="Save Information", font=("Ariel", 15), command=save_info, fg="#516BEB")
add_btn.grid(row=5, column=1, columnspan=2)
add_btn.config(padx=8, pady=4)

window.mainloop()
