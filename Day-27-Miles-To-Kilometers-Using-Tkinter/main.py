import tkinter

DEFAULT_PADDING = 5

window = tkinter.Tk()

window.title("Miles to Kilometers")
window.config(padx=20, pady=20)

# Row 0
input_miles = tkinter.Entry(width=10)
input_miles.focus()  # Puts cursor in textbox.
input_miles.insert(tkinter.END, string="0")
input_miles.grid(row=0, column=1, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0, column=2, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

# Row 1
label_is_equal_to = tkinter.Label(text="is equal to")
label_is_equal_to.grid(row=1, column=0, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

label_calc_km = tkinter.Label(text="0")
label_calc_km.grid(row=1, column=1, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

label_km = tkinter.Label(text="Km")
label_km.grid(row=1, column=2, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)


# Row 2
def convert_miles_to_km():
    result = round(float(input_miles.get()) * 1.609, 2)
    label_calc_km.config(text=f"{result}")


button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
button.grid(row=2, column=1, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

window.mainloop()
