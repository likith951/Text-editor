from tkinter import *
from functools import partial


def togglebnt(buttons, bnt, frames):
    for button in buttons:
        if button == bnt:
            button.config(relief=SUNKEN)
            frames[buttons.index(button)].grid(row=1, column=1)
        else:
            button.config(relief=RAISED)
            frames[buttons.index(button)].grid_forget()


def expenTemplate():
    win = Tk()
    win.geometry("300x300")
    win.resizable(1, 1)
    win.title("ExpenTemplate")
    win.configure(background="White")

    win.columnconfigure(index=0, weight=1)
    win.columnconfigure(index=1, weight=1)
    win.columnconfigure(index=2, weight=1)

    dayB = Button(win, text="DAY EXPENSE", bg="White", fg="Black", relief=SUNKEN)
    dayB.grid(row=0, column=0, sticky=NSEW)
    weekB = Button(win, text="WEEK EXPENSE", bg="White", fg="Black", relief=RAISED)
    weekB.grid(row=0, column=1, sticky=NSEW)

    monthB = Button(win, text="MONTH EXPENSE", bg="White", fg="Black", relief=RAISED)
    monthB.grid(row=0, column=2, sticky=NSEW)

    buttons = [dayB, weekB, monthB]

    dayF = Frame(win, padx=10, pady=10, bg="white")
    weekF = Frame(win, padx=10, pady=10, bg="white")
    monthF = Frame(win, padx=10, pady=10, bg="white")
    frames = [dayF, weekF, monthF]
    dayF.grid(row=1, column=0, sticky=NSEW)
    # DAY FRAME
    dayL = Label(dayF, text="day Lable", padx=10, pady=10, bg="white")
    dayL.grid(row=1, column=0, sticky=NSEW)
    # WEEK FRAME
    weekL = Label(weekF, text="weekLable", padx=10, pady=10, bg="white")
    weekL.grid(row=1, column=0, sticky=NSEW)
    # MONTH FRAME
    monthL = Label(monthF, text="monthLable", padx=10, pady=10, bg="white")
    monthL.grid(row=1, column=0, sticky=NSEW)
    for button in buttons:
        button.config(command=partial(togglebnt, buttons, button, frames))

    togglebnt(buttons, dayB, frames)
    win.mainloop()