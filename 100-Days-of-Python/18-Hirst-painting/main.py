###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

#print(rgb_colors)

color_list = [(202, 164, 109), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

#painting 10x10 of spots
#dots = 20 size, spacing = 50 paces

#create turtle object; set speed; specify that the pen is up (not drawing during movement); hide turtle; set color mode to RGB; set initial position coordinates
hirst = t.Turtle()
hirst.speed(10)
hirst.pu()
hirst.hideturtle()
t.colormode(255)
position = [-200,-200]

def draw_10_dots(coords):
    hirst.setposition(coords)
    for n in range(10):
        hirst.dot(20, random.choice(color_list))
        hirst.forward(50)
    coords[1] +=50
    hirst.setposition(coords)

for _ in range(10):
    draw_10_dots(position)


screen = t.Screen()
screen.exitonclick()
