from tkinter import *
root = Tk()
root.title("Simple Calculator")


# Creating a Input field
e= Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0,columnspan=3,  padx=10, pady=10)
e.pack()
e.get()

def button_add():
    pass

#e.insert(0,"Enter your name")

# Define Button
button_1 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_2 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_3 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_4 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_5 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_6 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_7 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_8 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_9 = Button(root, text=1, padx=40, pady=20, command= button_add)
button_0 = Button(root, text=1, padx=40, pady=20, command= button_add)

# Put Button on the Screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)


button_0 .grid(row=4, column=0)




root.mainloop()