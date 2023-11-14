"""22_Purna_Bahadur_Saud_Assignment-01.py: Description of simple notepad text editor."""

__author__      = "Purna Bahadur Saud"
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def about():
    tmsg.showinfo("About", "This is made by Purna Saud")


def cut():
    Textwindow.focus_get().event_generate("Cut")


def copy():
    Textwindow.focus_get().event_generate("Copy")


def paste():
    Textwindow.focus_get().event_generate("Paste")


def new():
    global file
    mainwindow.title("My Notepad")
    file = None
    Textwindow.focus_get().delete(1.0, END)


def open():
    global file
    file = askopenfilename(defaultextension=".txt",
                        filetypes=[("All Files", "*.*"),
                        ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        mainwindow.title(os.path.basename(file) + " - My Notepad")
        Textwindow.delete(1.0, END)
        f = open(file, "r")
        Textwindow.insert(1.0, f.read())
        f.close()


def save():
    global file
    if file == None:

        file = asksaveasfilename(initialfile = 'Untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:

            f = open(file, "w")
            f.write(Textwindow.get(1.0, END))
            f.close()

            mainwindow.title(os.path.basename(file) + " - My Notepad")

    else:

        f = open(file, "w")
        f.write(Textwindow.get(1.0, END))
        f.close()

mainwindow = Tk()
mainwindow.geometry("650x450")
mainwindow.title("My Notepad")

Textwindow=Text(mainwindow)
Textwindow.pack(expand="True", fill=BOTH)

Addscroll=Scrollbar(Textwindow)
Addscroll.pack(side=RIGHT, fill=Y)
Addscroll.config(command=Textwindow.yview)
Textwindow=Text(mainwindow, yscrollcommand=Addscroll.set)

thismenu = Menu(mainwindow)
mainwindow.config(menu=thismenu)

file = Menu(thismenu)
thismenu.add_cascade(label='File', menu=file)
file.add_command(label='New', command=new)
file.add_command(label='Open', command=open)
file.add_command(label='Save', command=save)
file.add_separator()
file.add_command(label='Exit', command=mainwindow.quit)

Edit = Menu(thismenu)
thismenu.add_cascade(label="Edit", menu=Edit)
Edit.add_command(label='Cut', command=cut)
Edit.add_command(label='Copy', command=copy)
Edit.add_command(label='Paste', command=paste)

help = Menu(thismenu)
thismenu.add_cascade(label="Help", menu=help)
help.add_command(label='About', command=about)

mainwindow.mainloop()