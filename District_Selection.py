
"""District_Selection.py: Description of Selection Of District From each province."""

__author__      = "Purna Bahadur Saud"

import os
import csv
from tkinter import *
from tkinter import messagebox
os.chdir("C:/Users/Dell\Desktop/22_Purna_Saud_Assignment-02/22_Purna_Bahadur_Saud_python-Assignment-02")

# Reading Data from a CSV file specified at a given Location
def readCSV(f):
    d = dict()
    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for col1, col2 in csv_reader:
            d[col1] = col2
    root1 = Tk()
    v = StringVar(root1)
    val = list(d.values())
    v.set(val[0])

    def showchoice():
        val = v.get()

        messagebox.showinfo(title='District Code', message='Code :{}'.format(val))

    Label(root1, text="""Choose your District""", justify=LEFT, padx=20).pack()
    for i in d.keys():
        Radiobutton(root1, text=i, padx=20, variable=v, command=showchoice, value=d[i]).pack(anchor=W)
    mainloop()


root = Tk()
v = IntVar()
v.set(1)

# Defining functions to get value from a radiobutton
def showchoice():
    val = v.get()
    if val == 1:
        readCSV('excelpy.csv')
    elif val == 2:
        readCSV('excelpy2.csv')
    elif val == 3:
        readCSV('excelpy3.csv')
    elif val == 4:
        readCSV('excelpy4.csv')
    elif val == 5:
        readCSV('excelpy5.csv')
    elif val == 6:
        readCSV('excelpy6.csv')
    elif val == 7:
        readCSV('excelpy7.csv')


province_list = [("Province1", 1), ("Province2", 2), ("Province3", 3), ("Province4", 4), ("Province5", 5),
                 ("Province6", 6), ("Province7", 7)]
Label(root, text="""Choose Province in which your District lies""", justify=LEFT, padx=20).pack() # Label
# Radio Button of each province
for i, j in province_list:
    Radiobutton(root, text=i, padx=20, variable=v, command=showchoice, value=j).pack(anchor=W)
mainloop()