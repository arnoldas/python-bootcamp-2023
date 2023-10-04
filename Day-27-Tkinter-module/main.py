import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # add more space between items

# Create a Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
#my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20) # add space around the label

# Change label text (update label properties)
my_label["text"] = "Changed label text"
my_label.config(text="New Text")


# Create a button
def button_clicked():
    my_label.config(text=input.get())
    print("I got clicked")


button = tkinter.Button(text="Click me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New button")
new_button.grid(column=2, row=0)

# Create input field (entry)
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
#input.pack()
#input.place(x=0, y=0)


#

window.mainloop()
