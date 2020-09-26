# Importing modules
from tkinter import *
from tkinter import ttk
from os.path import isfile
import mod1

# Defining variables
with open("info.dat","rb") as file:
    file_info = mod1.decrypt(file.read())

if isfile("readme.md"):
    with open("readme.md","r") as file:
        readme_stuff = file.read()
else:
    readme_stuff = "readme.md does not exist"

with open("1611625.bin","rb") as file:
    correct_password = str(mod1.decrypt(file.read()))
    correct_password = correct_password[:-1]

def refresh(*args):
    with open("info.dat","rb") as file:
        password_output.delete(0.0,END)
        password_output.insert(0.0,mod1.decrypt(file.read()))

# Defining functions
def send(*args):
    password = passkey.get()

    if password == correct_password:
        input.delete(0,END)
        password_output.delete(0.0,END)
        pass_out_save.configure(state=ACTIVE)
        password_output.configure(state=NORMAL)
        password_output.bind("<Control-s>",save)
        password_output.bind("<Control-S>",save)
        refresh()
    else:
        pass

def save(*args):
    text = password_output.get(0.0,END)
    corr_pass = mod1.encrypt(text[:text.find("\n")+1])

    with open("info.dat","wb") as file:
        file.write(mod1.encrypt(text))
    with open("1611625.bin","wb") as file:
        file.write(corr_pass)

    refresh()

#------------------------Main GUI code------------------------#
win = Tk()
win.title('Information SAFE')
passkey = StringVar()

# Row 1 widgets
text1 = ttk.Label(win,text="Password :")
text1.grid(row=1,column=0,sticky=W)
input = ttk.Entry(win,width=30,textvariable=passkey)
input.focus()
input.bind("<Return>",send)
input.grid(row=1,column=1,sticky=W)

# Row 2 widgets
send_button = ttk.Button(win,text="Enter",command=send)
send_button.grid(row=2,column=0,sticky=W)

# Row 3 widgets
password_output = Text(win,height=10,width=70,wrap=WORD)
password_output.grid(row=3,columnspan=100,sticky=W)
password_output.insert(0.0,readme_stuff)
password_output.configure(state=DISABLED)

# Row 4 widgets
pass_out_save = ttk.Button(win,text="Save",state=DISABLED,command=save)
pass_out_save.grid(row=4,column=0)

win.mainloop()