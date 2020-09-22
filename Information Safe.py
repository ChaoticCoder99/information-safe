from tkinter import *
from tkinter import ttk
import mod1

with open("info.dat","rb") as file:
    file_info = mod1.decrypt(file.read())

with open("readme.md","r") as file:
    readme_stuff = file.read()

with open("1611625.bin","rb") as file:
    correct_password = str(mod1.decrypt(file.read()))
    correct_password = correct_password.rstrip("\n")

def refresh(*args):
    with open("info.dat","rb") as file:
        password_output.delete(0.0,END)
        password_output.insert(0.0,mod1.decrypt(file.read()))

def send(*args):
    password = passkey.get()

    if password == correct_password:
        input.delete(0,END)
        password_output.delete(0.0,END)
        refresh()
        pass_out_save.configure(state=ACTIVE)
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

win = Tk()
win.title('Password Storer')
passkey = StringVar()

text1 = ttk.Label(win,text="Enter The Passkey :")
text1.grid(row=1,column=0,sticky=W)
input = ttk.Entry(win,width=30,textvariable=passkey)
input.focus()
input.bind("<Return>",send)
input.grid(row=1,column=1,sticky=W)

send_button = ttk.Button(win,text="Enter",command=send)
send_button.grid(row=2,column=0,sticky=W)

password_output = Text(win,height=10,width=70,wrap=WORD)
password_output.grid(row=3,columnspan=100,sticky=W)
password_output.insert(0.0,readme_stuff)
password_output.bind("<Control-s>",save)
password_output.bind("<Control-S>",save)

pass_out_save = ttk.Button(win,text="Save",state=DISABLED,command=save)
pass_out_save.grid(row=4,column=0)

win.mainloop()
