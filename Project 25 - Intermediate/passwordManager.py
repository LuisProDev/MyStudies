from tkinter import *
from tkinter import messagebox
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    info = [website, " | ", email, " | ", password, "\n"]

    if len(website) == 0 and len(password) == 0 and len(email) == 0:
        messagebox.showwarning(message=f"Please don't leave fields empty!")

    else:
        check = messagebox.askokcancel(title="Confirm",
                                       message=f"These are the details you entered: "
                                       f"\nEmail: {email}, "
                                       f"\nPassword: {password}"
                                       f"\nIs it ok to save?")
        if check:
            current_dir = os.getcwd()
            output_file_name = current_dir + "\passwords.txt"
            with open(output_file_name, "a+") as password_file:
                password_file.writelines(info)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus_set()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.resizable(False, False)
window.config(padx=60, pady=15)

# Define the size and starting place of the window
window_height = 400
window_width = 600

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Design the logo
canvas = Canvas(width=200, height=224)
lock_image = PhotoImage(file=resource_path("logo.png"))
canvas.create_image(110, 112, image=lock_image)
canvas.grid(row=0, column=1)

# Create labels
website_label = Label(text="Website:", font=("Futura", 10, "normal"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Futura", 10, "normal"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Futura", 10, "normal"))
password_label.grid(row=3, column=0)

# Create Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus_set()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=41)
password_entry.grid(row=3, column=1)

# Create Buttons
generate_button = Button(text="Generate", font=("Futura", 10, "normal"))
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", font=("Futura", 10, "normal"), width=38, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
