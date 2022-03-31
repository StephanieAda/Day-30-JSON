from tkinter import *
from tkinter import messagebox
from Password_Generator import PasswordGenerator
import json

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# ---------------------------- SAVE PASSWORD -------------------------------


def search_websites():
    try:
        with open('data.json', 'r') as file:
            website = website_entry.get().title()
            print(website)
            website_data = json.load(file)
            username_data = website_data[website]['username']
            password_data = website_data[website]['password']
            messagebox.showinfo(title=website, message=f'Username:{username_data} \n Password:{password_data}')
    except KeyError:
        messagebox.showinfo(title='Does Not Exist', message=f'No available entry for {website}')


def add_data():
    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    data_dict = {
        website: {
            "username": username,
            "password": password
        }
    }

    # if not website.isalnum() or not password.isalnum() or not username.isalnum():
    #     print('Yeah')
    # print("done")
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Missing Information', message='Some fields are empty!')

    else:
        try:
            with open('data.json', 'r') as file:
                # Reading old data
                data_file = json.load(file)
                # Updating old data with new data
                data_file.update(data_dict)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(data_dict, file, indent=4)
        else:
            with open('data.json', 'w') as file:
                # Saving updated data
                json.dump(data_file, file, indent=4)
        finally:
            print('done')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo - Copy.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_label.grid(row=2, column=0)
website_entry = Entry(width=25)
website_entry.lower()
website_entry.grid(row=2, column=1)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=0)
username_entry = Entry(width=50)
username_entry.grid(row=3, column=1, columnspan=2)
username_entry.insert(0, 'elluhstephanie4good@gmail.com')

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=4, column=1)
password_maker = PasswordGenerator(password_entry)
generate_password = Button(text='Generate Password', width=20, command=password_maker.generate_password)
generate_password.grid(row=4, column=2)

add_button = Button(text="Add", width=45, command=add_data)
add_button.grid(row=5, column=1, columnspan=2)

search_button = Button(text="Search", width=20, command=search_websites)
search_button.grid(row=2, column=2)
window.mainloop()
