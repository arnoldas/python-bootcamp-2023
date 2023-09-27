import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=750, height=520)

# Function returns coordinates from mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

total_guesses = len(data["state"])

prompt_text = "What's another state's name?"
while len(guessed_states) < total_guesses:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_guesses} States Correct",
                                    prompt=prompt_text).title().strip()

    if answer_state == "Exit":
        # Generate CSV file which states are not guessed
        print(all_states)
        print(guessed_states)
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")  # Creating new CSV file
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"].iloc[0]), int(state_data["y"].iloc[0]))
        t.write(answer_state) # or we can get value using t.write(state_data["state"].item())
