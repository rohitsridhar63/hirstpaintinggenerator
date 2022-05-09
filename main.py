# import colorgram
#
#
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
'''importing modules'''
import turtle
import random

'''changing the color mode to accept rgb instead of color string'''
turtle.colormode(255)

'''function to choose a random color from the given list of rgb values'''


def random_color():
    color_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40),
                  (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93),
                  (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]
    mc = random.choice(color_list)
    return mc


'''creating the object called draw_bot out of the turtle class'''
draw_bot = turtle.Turtle()

'''initializing the turtle starting point and speed'''
draw_bot.hideturtle()  # hiding the turtle so that we cannot see it, it is still there though
draw_bot.penup()  # pen is up so that it does not draw lines in its path
draw_bot.setheading(225)
draw_bot.forward(300)
draw_bot.setheading(0)
draw_bot.speed('fastest')

'''loop for the turtle path'''
for i in range(10):
    for j in range(10):
        draw_bot.pencolor(random_color())

        draw_bot.dot(20)
        draw_bot.penup()
        draw_bot.forward(50)

    draw_bot.left(90)
    draw_bot.forward(50)
    draw_bot.right(90)
    draw_bot.backward(500)

'''screen initialization'''
screen = turtle.Screen()
screen.exitonclick()
