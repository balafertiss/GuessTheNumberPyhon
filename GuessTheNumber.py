from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random

Flag1 = 0
Tries = 0
Rnumber = 10000000

window = ThemedTk(theme = "yaru")
window.configure(themebg="yaru")
window.geometry("700x500")

def Guess(event):
    global Rnumber
    global Tries

    if Flag1 == 1:
        Try = int(Guessent.get())
        Startbtn["state"] = "disable"

        if Try < Rnumber:
            Tries += 1
            Trieslbl.configure(text = "Tries:" + str(Tries))
            randomlbl.configure(image = upimg)
            Guessent.delete(0, END)
        elif Try > Rnumber:
            Tries += 1
            Trieslbl.configure(text="Tries:" + str(Tries))
            randomlbl.configure(image = downimg)
            Guessent.delete(0, END)
        else:
            randomlbl.configure(image = correctimg)
            Guessent["state"] = "disable"
            Startbtn.configure(text = "Restart")
            Startbtn["state"] = "normal"
            Guessent.delete(0, END)
    else:
        a=1


def Start():
    global Tries
    global Flag1
    Tries = 0
    Flag1 = 1
    Trieslbl.configure(text="Tries:" + str(Tries))
    randomlbl.configure(image = randomimg)
    Startbtn.configure(text="Start")
    Guessent["state"] = "normal"
    Guessent.delete(0,END)
    global Rnumber
    if rb.get() == "Easy":
        Rnumber = random.randint(0,20)
    elif rb.get() == "Medium":
        Rnumber = random.randint(0, 100)
    else:
        Rnumber = random.randint(0, 300)

randomimg = PhotoImage(file="Dice.png")
upimg = PhotoImage(file="Up.png")
downimg = PhotoImage(file="Down.png")
correctimg = PhotoImage(file="Correct.png")

lbl1 = ttk.Label(window,text = "Welcome to guess the number.\nChoose difficulty and press start to begin\nHave fun!!!",justify=CENTER,foreground = "#7E0A7E",font = ("Mangal", 20,'bold'))
lbl1.pack()

Trieslbl = ttk.Label(window,text = "Tries:" + str(Tries),foreground = "#7E0A7E",font = ("Mangal", 20,'bold'))
Trieslbl.place(x=308,y=400)

randomlbl = ttk.Label(window,image= randomimg)
randomlbl.place(x=10,y=315)


rb = StringVar()

rad1 = ttk.Radiobutton (window, text="Easy(0-20)", value="Easy", variable=rb,)
rad1.place(x=110 , y=160)

rad2 = ttk.Radiobutton (window, text="Medium(0-100)", value="Medium", variable=rb,)
rad2.place(x=297,y=160)

rad3= ttk.Radiobutton (window, text="Hard(0-300)", value="Hard", variable=rb,)
rad3.place(x=500,y=160)


Guessent = ttk.Entry(window,width = 10,state = "disabled")
Guessent.place(x=320,y=300)


Startbtn = ttk.Button(window,text = "Start",command = Start)
Startbtn.place(x=550,y=320)

Exittbtn = ttk.Button(window,text = "Exit",command = exit)
Exittbtn.place(x=550,y=400)


window.bind('<Return>',Guess)

window.mainloop()