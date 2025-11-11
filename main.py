#Main.py
import copy
from functools import partial
from tkinter import *
from tkinter import filedialog
from  editMenu import *
from viewMenu import *
global w , file , text
def newfile(event=None):
    filename = filedialog.asksaveasfilename()
    file = open(filename, "w")
    window(filename,file)


def openfile(event=None):
    filename = filedialog.askopenfilename()
    file = open(filename, "r+")
    content = file.read()
    window(filename,file,content)

def window(filename,file,content=""):
    w = Tk()
    w.title(filename)
    w.resizable(True, True)
    w.geometry("300x300")
    w.configure(background="white")


    text=Text(w)
    text.pack(fill=BOTH, expand=True,padx=5, pady=10, ipady=5)
    text.insert(INSERT,content)

    Llable = Label(w, text="Line:0|Col:0")
    Llable.place(relx=1.0, rely=1.0, anchor='se')
    Wlable=Label(w, text="Word:0|Character:0")
    Wlable.place(relx=0.0, rely=1.0, anchor='sw')
    text.bind("<KeyRelease>", partial(wordCount,Wlable,text,Llable))
    text.bind("<ButtonRelease>", partial(wordCount,Wlable,text,Llable))


    menubar = Menu(w)
    w.configure(menu=menubar)
    fileMenu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=newfile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Open", command=openfile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Save", command=partial(save,file,text))
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=w.destroy)

    editMenu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Edit", menu=editMenu)

    editMenu.add_command(label="Undo", command=undo)
    editMenu.add_separator()
    editMenu.add_command(label="Redo", command=redo)
    editMenu.add_separator()
    editMenu.add_command(label="Clear", command=partial(clear,file,text))
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

    def auto_save(w):
        save(file, text)
        w.after(30000, partial(auto_save,w))  # 30000 ms = 30 sec

    w.after(30000, partial(auto_save,w))

    w.mainloop()

    w.mainloop()

def save(file,text,event=None):
     file.seek(0)
     file.truncate(0)
     file.write(text.get(1.0, "end-1c"))
     file.flush()
def clear(file,text,event=None):
    text.delete(1.0, END)
    file.seek(0)
    file.truncate(0)
    file.write(text.get(1.0, END))
    file.flush()
def wordCount(Wlabel,text,Llable,event=None):
    words=text.get(1.0, "end-1c").split()
    wordCount = len(words)
    charCount = 0
    n = text.index(INSERT)
    l = n.split(".")
    Llable.config(text="Line:{}|Col:{}".format(l[0], l[1]))
    for word in words:
        for letter in word:
            charCount+=1
    Wlabel.config(text="Word:{}|Character:{}".format(wordCount,charCount))



def encryptfile(even=None):
    print("Encrypt File")
def decryptfile(even=None):
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
