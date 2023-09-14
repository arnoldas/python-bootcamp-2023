from turtle import Turtle

WIDTH = 20
HEIGHT = 100
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=HEIGHT / 20, stretch_len=WIDTH / 20)
        self.penup()
        self.setpos(position)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setpos(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.setpos(x=self.xcor(), y=new_y)
