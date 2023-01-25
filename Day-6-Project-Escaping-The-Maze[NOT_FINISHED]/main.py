def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_right()
    else:
        move()

# wall_in_front() == not front_is_clear
# wall_on_right() == not right_is_clear
# +++ at_goal()