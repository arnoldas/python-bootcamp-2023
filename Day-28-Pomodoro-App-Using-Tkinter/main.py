import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer", fg=GREEN)
    label_check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label_title.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reps = 0
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    new_minutes = str(math.floor(count / 60)).rjust(2, "0")
    new_seconds = str(count % 60).rjust(2, "0")
    canvas.itemconfig(timer_text, text=f"{new_minutes}:{new_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            label_check_marks["text"] += "✔"


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# def say_something(thing):
#    print(thing)

# window.after(1000, say_something, "Hello there")

label_title = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "normal"))
label_title.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

label_check_marks = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "normal"))
label_check_marks.grid(row=3, column=1)

button_reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
