from json import JSONDecodeError
from random import choice
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------------ #
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title='Oops', message="Please don't leave Website blank")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showerror(title='Oops', message="Password file does not exist")
        else:
            print(data)
            for item in data:
                print(f"item is {item}")
                print(f"Website is {website}")
                if item == website:
                    print("it worked")
                    messagebox.showinfo(title=item, message=f"Email: {data[item]['email']} \nPassword: {data[item]['password']}")
                else:
                    messagebox.showinfo(title="Oops", message='No details for the website exists')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, 'end')
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password =  password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(password) < 1 or len(website) < 1:
        messagebox.showerror(title='Oops', message="Please don't leave empty fields")

    else:
        try:
            with open('data.json', mode='r') as data_file:
                #Reading old data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(new_data)

        except FileNotFoundError or JSONDecodeError:
            with open('data.json', 'w') as data_file:
                #write a new file if one doesn't exist
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            email_entry.insert(0, 'example_email@gmail.com')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.focus()
website_entry.grid(row=1, column=1, sticky='EW')

search_button = Button(text='Search', command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text='Email/Username:')
email_label.grid(row=2,column=0)

email_entry = Entry()
email_entry.insert(0, 'example_email@gmail.com')
email_entry.grid(row=2,column=1, sticky='EW', columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3,column=0)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='EW')

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3,column=2, sticky='EW')

add_button = Button(width=35, text='Add', command=save)
add_button.grid(row=4,column=1, columnspan=2, sticky='EW')

window.mainloop()