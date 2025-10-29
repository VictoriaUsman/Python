# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open('Keeper.txt', 'a') as file:
        web = entry.get()
        user = user_entry.get()
        password = password_entry.get()
        pyperclip.copy(password)
        new_json = {
            web: {
                "Email": user,
                "Password": password,
            }
        }
        messagebox.showinfo(title = f"Save the file", message = f"Here are the information to save: Website: {web}\nUsername: {user}\nPassword: {password}")
        try:
            with open("Keeper.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_json)

            with open("Keeper.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except:
            with open("Keeper.json", "w") as data_file:
                json.dump(new_json, data_file, indent=4)

        finally:
            entry.delete(0, END)
            user_entry.delete(0, END)
            password_entry.delete(0, END)
            user_entry.insert(0, "iantrisdc@gmail.com")






# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox
import pyperclip


def search():
    search = entry.get()
    with open('Keeper.json', 'r') as file:
        data = json.load(file)
        passc = data[search]["Password"]
        messagebox.showinfo(title = "Password Retrieved", message = f"Here is you password for {search}:\n{passc}" )


lockit = Tk()
lockit.title("Passlock by Ian TrisDC")
lockit.config(width=800, height=500, bg = "white")
lockit.config(bg="white")
logo = PhotoImage(file="finallogo.png")
canvas = Canvas(width=800, height=500, bg="white")
canvas.create_image(400, 150, image=logo)
canvas.create_text(397,240, text = "by Ian Tristan Cultura",)
canvas.place(x=0, y=0)

#Entry Website
websitelabel = Label(lockit, text="Website:", bg="white")
websitelabel.place(x=193, y=350)
entry = Entry(width=40)
entry.insert(0, "Your Website Here...")
entry.focus()
entry.place(x=260, y=348)

#Add Button
add_button = Button(text="Add to List", bg="blue", fg="blue", highlightthickness=0, command=save)
add_button.place(x=290, y=450)

#Search Button
add_button = Button(text="Search", bg="blue", fg="blue", highlightthickness=0, command=search)
add_button.place(x=420, y=450, width=120)

#Username Entry
user_entry = Entry(width=40)
user_entry.insert(0, "iantrisdc@gmail.com")
user_entry.place(x=260, y=380)
userlabel = Label(text="Email/Username:", bg="white")
userlabel.place(x=145, y=381)

#Password
password_entry = Entry(width=20)
password_entry.insert(0, "Your password here...")
password_entry.place(x=260, y=412)
passwordlabel = Label(text="Password:", bg="white")
passwordlabel.place(x=184, y=413)

def password():
    import random
    password_entry.delete(0, END)  # clear previous text

    letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!#$%&()*+')

    passcode = []
    for _ in range(5):
        passcode.append(random.choice(letters))
    for _ in range(5):
        passcode.append(random.choice(symbols))
    for _ in range(5):
        passcode.append(random.choice(numbers))

    random.shuffle(passcode)  # shuffle list before joining
    new_password = "".join(passcode)

    password_entry.insert(0, new_password)


#Generate Button
genpass = Button(text="Generate Password", bg="blue", fg="blue", highlightthickness=0, command=password)
genpass.place(x=460, y=412)






lockit.mainloop()
