from tkinter import *

window = Tk()

red_label = Label(bg="red", width=20, height=5)
red_label.grid(row=0, column=0)

green_label = Label(bg="green", width=20, height=5)
green_label.grid(row=1, column=1)

blue_label = Label(bg="blue", width=40, height=5)
blue_label.grid(row=2, column=0, columnspan=2)

window.mainloop()
