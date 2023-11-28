import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv", usecols=["French", "English"])
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv", usecols=["French", "English"])
else:
    datadict = data.to_dict(orient="records")


def flip_card():
    global current_card
    canvas.itemconfig(canvas_background, image=canvas_image_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel existing timer
    current_card = random.choice(datadict)
    canvas.itemconfig(canvas_background, image=canvas_image_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)  # Create a new timer for new card


def is_known():
    datadict.remove(current_card)  # Remove from the word list known word
    new_data = pandas.DataFrame(datadict)  # Create new data frame with unknown words
    new_data.to_csv("data/words_to_learn.csv", index=False)  # Create new csv file without index numbers
    next_card()


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a time, which after 3s executes flip_card method
flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526)
canvas_image_front = tkinter.PhotoImage(file="images/card_front.png")
canvas_image_back = tkinter.PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=canvas_image_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, sticky="EW")

cross_image = tkinter.PhotoImage(file="images/wrong.png")
cross_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_image = tkinter.PhotoImage(file="images/right.png")
check_button = tkinter.Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()
