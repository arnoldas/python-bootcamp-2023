from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments_array = []
        self.create_snake()

    def create_snake(self):
        default_length = 3
        default_x = 0
        default_size = 20
        for i in range(default_length):
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=default_x, y=0)
            default_x += -default_size
            self.segments_array.append(turtle)

    def move(self):
        for i in range(len(self.segments_array) - 1, 0, -1):
            new_x = self.segments_array[i - 1].xcor()
            new_y = self.segments_array[i - 1].ycor()
            self.segments_array[i].goto(x=new_x, y=new_y)
        self.segments_array[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments_array[0].heading() != DOWN:
            self.segments_array[0].setheading(UP)

    def down(self):
        if self.segments_array[0].heading() != UP:
            self.segments_array[0].setheading(DOWN)

    def left(self):
        if self.segments_array[0].heading() != RIGHT:
            self.segments_array[0].setheading(LEFT)

    def right(self):
        if self.segments_array[0].heading() != LEFT:
            self.segments_array[0].setheading(RIGHT)
