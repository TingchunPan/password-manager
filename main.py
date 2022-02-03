from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    # print(f"Your password is: {password}")
    entryPass.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    entry_new = entry.get()
    entryEmail_new=entryEmail.get()
    entryPass_new=entryPass.get()

    if len(entry_new) == 0 or len(entryPass_new) == 0 or len(entryPass_new) == 0:
        messagebox.askokcancel(title="Oops", message=f"Please don't leave any fields empty!")


    else:
        is_ok = messagebox.showinfo(title=entry_new,
                                       message=f"The details entered are here: \nEmail: {entryEmail_new}"
                                               f"\nPassword: {entryPass_new} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{entry_new} | {entryEmail_new} | {entryPass_new}\n")
                entry.delete(0, END)
                entryEmail.delete(0, END)
                entryPass.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.pack()
# timer_text=canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=0)

label=Label()
label.config(text="Website:")
label.grid(column=0,row=1)

Email=Label()
Email.config(text="Email/Username:")
Email.grid(column=0,row=2)

password=Label()
password.config(text= "Password:")
password.grid(column=0,row=3)

entry=Entry()
entry.config(width=35)
entry.grid(column=1,row=1,columnspan=2)

entryEmail=Entry()
entryEmail.config(width=35)
entryEmail.grid(column=1,row=2,columnspan=2)

entryPass=Entry()
entryPass.config(width=21)
entryPass.grid(column=1,row=3)


button=Button()
button.config(text="Generate Password",command=generate_password)
button.grid(column=2,row=3)

addButton=Button()
addButton.config(text="Add",width=36,command=save)
addButton.grid(column=1,row=4,columnspan=2)


window.mainloop()


