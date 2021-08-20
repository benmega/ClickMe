import time

import tkinter as tk
import random
from tkinter import messagebox


def youWin():
    global  start, top, level
    score = time.time() - start
    start = time.time()
    messagebox.showinfo("Ben Mega Creations",f'You Win! It took you {round(score,2)} seconds.')
    top.destroy()
    level += 1
    top = startLevel(level)
    top.mainloop()


def button_hover(event):
    global buttonRelX, buttonRelY, textNum
    curBut = event.widget
    buttonRelX += random.random()
    if buttonRelX >= 0.8:
        buttonRelX = 0.1
    buttonRelY += random.random()
    if buttonRelY >= 0.8:
        buttonRelY = 0.1
    curBut.place(relx=buttonRelX,rely=buttonRelY)
    buttons[0]["bg"] = "red"
    textNum = (textNum +1) %len(futureTexts)
    text.set(futureTexts[textNum])


def addButton(event):
    global i, top
    buttons.append(tk.Button(top, wraplength=50, textvariable=text, command=lambda i=len(buttons): buttons[i].destroy(), width=10, height=5))
    buttons[-1].place(relx=random.random(), rely=random.random())
    buttons[-1].bind("<Enter>", button_hover)


def startLevel(level, width=500, height=500):
    global start, text, textNum, futureTexts, i, buttonRelX, buttonRelY, buttons
    newWindow = tk.Toplevel()
    newWindow.geometry(f"{width}x{height}")
    newWindow.minsize(width=width, height=height)
    newWindow.bind('<Button-1>', addButton)
    text = tk.StringVar()
    text.set("Click me")
    textNum = 0
    futureTexts = ['come on, just click me!', 'What''s wrong?', 'You missed', 'You missed again',
                   'This is starting to get embarrasing', 'Ok, I won''t move', 'sorry, I lied']
    buttons = []
    i = 0
    buttons.append(tk.Button(newWindow, wraplength=50, textvariable=text, command=youWin, width=int(60*0.8**level), height=int(30*0.8**level)))
    buttonRelX = 0.2
    buttonRelY = 0.2
    buttons[0].place(relx=buttonRelX, rely=buttonRelY)
    buttons[0].bind("<Enter>", button_hover)
    newWindow.protocol("WM_DELETE_WINDOW", on_closing)
    start = time.time()
    return newWindow


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()



root = tk.Tk()
root.withdraw()

level = 1
top = startLevel(1)
top.mainloop()