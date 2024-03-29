from turtle import Turtle

DEFAULT_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = DEFAULT_SPEED
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = DEFAULT_SPEED
        self.setpos(x=0, y=0)
        self.bounce_x()
