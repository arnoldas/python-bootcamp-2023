import colorgram
import turtle as turtle_module
import random

def get_rgb_colors_from_image(p_image):
    number_of_colors = 30
    rgb_colors = []

    # read the colors from image
    colors = colorgram.extract(p_image, number_of_colors)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        # don't add blank colors into list
        if not (r >= 230 and g >= 230 and b >= 230):
            rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return rgb_colors


#colors_list = get_rgb_colors_from_image('image.jpg')
#print(colors_list)

colors_list = [(222, 232, 225), (207, 160, 83), (54, 89, 131), (145, 91, 40), (139, 27, 48), (222, 206, 108), (132, 177, 203), (157, 46, 83), (46, 55, 103), (168, 159, 40), (128, 188, 143), (83, 20, 44), (37, 43, 68), (186, 93, 106), (185, 139, 172), (84, 123, 181), (59, 39, 31), (79, 153, 165), (88, 156, 91), (194, 79, 72), (45, 74, 77), (161, 201, 220), (80, 73, 44), (62, 127, 120), (219, 175, 186), (168, 206, 169), (221, 181, 167)]
turtle = turtle_module.Turtle()
turtle_module.colormode(255)
# print(random.choice(colors_list))

turtle.setheading(225)
turtle.penup()
turtle.hideturtle()
turtle.forward(250)
turtle.setheading(0)

def draw_row():
    for _ in range(10):
        turtle.dot(20, random.choice(colors_list))
        turtle.forward(50)

def goto_new_row():

    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    for _ in range(10):
        turtle.forward(50)
    turtle.right(180)

for _ in range(10):
    draw_row()
    goto_new_row()


screen = turtle_module.Screen()
screen.exitonclick()