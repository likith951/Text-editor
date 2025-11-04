#Main.py
from tkinter import *

def newfile():
    print("New File")

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
Bopenfile=Button(win,text="Open File",command=newfile,bg="grey",fg="white")
BExit=Button(win,text="Exit",command=win.destroy,bg="orange",fg="white")
Bencrypt=Button(win,text="Encrypt",command=win.destroy,bg="brown",fg="white")
Bdcrypt=Button(win,text="Decrypt",command=win.destroy,bg="red",fg="white")


Bnewfile.grid(row=0,column=0, padx=10,pady=2,sticky=NSEW)
Bopenfile.grid(row=1,column=0, padx=10,pady=2,sticky=NSEW)
Bencrypt.grid(row=2,column=0, padx=10,pady=2,sticky=NSEW)
Bdcrypt.grid(row=3,column=0, padx=10,pady=2,sticky=NSEW)
BExit.grid(row=4,column=0, padx=10,pady=2,sticky=NSEW)




win.mainloop()



win.mainloop()
