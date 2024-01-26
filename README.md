# GuessTheNumberPyhon
Created for fun. Dont hate. Amuteur work done for exercise.Feel free to write ideas to make the game better.Have fun.

from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random
import pyperclip

low = "abcdefghijklmnopqrstuvwxyz"
medium ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
strong ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789"

diff = "a"

def Generate():
    length = int(combo.get())
    b = ""
    if rb.get() == "Low":
        diff = low
    elif rb.get() == "Medium":
        diff = medium
    else:
        diff = strong
    for i in range(0,length,1):
        a = random.choice(diff)
        b = b+a
        Passent.delete(0,END)
        Passent.insert(0,b)

def Copy():
    txt = Passent.get()
    pyperclip.copy(txt)
def Copy2():
    txt = PassEncent.get()
    pyperclip.copy(txt)
def Encrypt():
    password = int(Passent.get())
    for i in range(0,password,1):


window = ThemedTk(theme = "yaru")
window.configure(themebg="yaru")
window.geometry("505x100")

Passlbl = ttk.Label(window,text = "Password:")
Passlbl.grid()

Lengthlbl = ttk.Label(window,text = "Length:")
Lengthlbl.grid()

PassEnc = ttk.Label(window,text = "Password Encrypted:")
PassEnc.grid()


Passent = ttk.Entry(window,width = 23)
Passent.grid(column = 1,row = 0)

PassEncent = ttk.Entry(window,width = 23)
PassEncent.grid(column = 1,row = 2)


combo = ttk.Combobox(window)
combo.grid(column = 1,row = 1)
combo ['values']= (6,7,8,9,10,11,12)
combo.current(0)


Generatebtn = ttk.Button(window,text = "Generate",command = Generate)
Generatebtn.grid(column = 3,row = 0)

Encryptbtn = ttk.Button(window,text = "Encrypt",command = Encrypt)
Encryptbtn.grid(column = 3,row = 2)

Copybtn = ttk.Button(window,text = "Copy", command = Copy)
Copybtn.grid(column = 4,row = 0)

Copybtn2 = ttk.Button(window,text = "Copy",command = Copy2)
Copybtn2.grid(column = 4,row = 2)

Decryptbtn = ttk.Button(window,text = "Decrypt",)
Decryptbtn.grid(column = 5,row=2)


rb =StringVar()

LowRad = ttk.Radiobutton (window, text="Low", value="Low", variable=rb)
LowRad.grid(column=3, row=1)

MedRad = ttk.Radiobutton (window, text="Medium", value="Medium", variable=rb)
MedRad.grid(column=4,row=1)

StrRad= ttk.Radiobutton (window, text="Strong", value="Strong", variable=rb)
StrRad.grid(column=5, row=1)


window.mainloop()
