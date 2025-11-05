#Main.py
import copy
from tkinter import *
from tkinter import filedialog
from  editMenu import *
from viewMenu import *


def window(filename):
    w = Tk()
    w.title(filename)
    w.resizable(True, True)
    w.geometry("300x300")
    w.configure(background="white")

    menubar = Menu(w)
    w.configure(menu=menubar)
    fileMenu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=newfile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Open", command=openfile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Save", command=save)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=w.destroy)

    editMenu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Edit", menu=editMenu)

    editMenu.add_command(label="Undo", command=undo)
    editMenu.add_separator()
    editMenu.add_command(label="Redo", command=redo)
    editMenu.add_separator()
    editMenu.add_command(label="Clear", command=clear)
    editMenu.add_separator()
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_separator()
    editMenu.add_command(label="cut", command=cut)
    editMenu.add_separator()
    editMenu.add_command(label="Find", command=find)
    editMenu.add_separator()
    editMenu.add_command(label="Find and search", command=findandsearch)

    viewMenu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="View", menu=viewMenu)

    viewMenu.add_command(label="Theme", command=changetheme)
    viewMenu.add_separator()
    viewMenu.add_command(label="Font Size", command=fontsize)
    viewMenu.add_separator()

    text=Text(w)
    text.pack(fill=BOTH, expand=True,padx=5, pady=10, ipady=5)

    Llable = Label(w, text="Line:0|Col:0")
    Llable.place(relx=1.0, rely=1.0, anchor='se')
    Wlable=Label(w, text="Word:0|Character:0")
    Wlable.place(relx=0.0, rely=1.0, anchor='sw')


    w.mainloop()

def save():
    print("Save func triggered")
def newfile():
    filename = filedialog.asksaveasfilename()
    file = open(filename, "w")
    window(filename)


def openfile():
    filename = filedialog.askopenfilename()
    file = open(filename, "w")
    window(filename)

def encryptfile():
    print("Encrypt File")
def decryptfile():
    print("Decrypt File")

win=Tk()
win.geometry("300x300")
win.title("Text Editor")
win.configure(bg="black")
win.resizable(True,True)

win.grid_rowconfigure(index=2,weight=1)
win.grid_rowconfigure(index=3,weight=1)
win.grid_rowconfigure(index=0,weight=1)
win.grid_rowconfigure(index=1,weight=1)
win.grid_rowconfigure(index=4,weight=1)
win.grid_columnconfigure(index=0,weight=1)


Bnewfile=Button(win,text="New File",command=newfile,bg="green",fg="white")
Bopenfile=Button(win,text="Open File",command=openfile,bg="grey",fg="white")
BExit=Button(win,text="Exit",command=win.destroy,bg="orange",fg="white")
Bencrypt=Button(win,text="Encrypt",command=encryptfile,bg="brown",fg="white")
Bdcrypt=Button(win,text="Decrypt",command=decryptfile,bg="red",fg="white")


Bnewfile.grid(row=0,column=0, padx=10,pady=2,sticky=NSEW)
Bopenfile.grid(row=1,column=0, padx=10,pady=2,sticky=NSEW)
Bencrypt.grid(row=2,column=0, padx=10,pady=2,sticky=NSEW)
Bdcrypt.grid(row=3,column=0, padx=10,pady=2,sticky=NSEW)
BExit.grid(row=4,column=0, padx=10,pady=2,sticky=NSEW)




win.mainloop()



win.mainloop()
