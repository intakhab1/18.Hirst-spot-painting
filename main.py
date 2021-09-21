# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_color = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(194, 160, 120), (72, 92, 125), (143, 87, 59), (216, 209, 122), (140, 160, 188), (183, 147, 162), (29, 33, 46), (119, 73, 92), (56, 35, 26), (174, 160, 42), (139, 174, 153), (78, 115, 80), (62, 30, 40), (139, 27, 18), (118, 29, 40), (182, 101, 87),
              (47, 59, 92), (174, 99, 115), (102, 120, 167), (33, 51, 45), (103, 155, 87), (214, 176, 190), (216, 181, 174), (66, 83, 28), (164, 208, 188), (182, 187, 212)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()