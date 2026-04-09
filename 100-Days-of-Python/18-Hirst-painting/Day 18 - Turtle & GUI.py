import turtle as t
import random 

# timmy = t.Turtle()
# timmy.shape("turtle")
# timmy.color("coral")

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for i in range(50):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

#Polygons
#my attempt --> nested for loop, couldn't get colors to alternate
color_list = ['chocolate','aquamarine','DeepPink','green','red','DarkSeaGreen','purple','CornflowerBlue']

# sides = 3
# for n in range(8):
#     timmy.color = color_list [n-1]
#     for i in range(sides):
#         timmy.forward(100)  
#         timmy.right(360/sides) 
#     sides +=1


#instructor solution --> create a function then make a for loop
# tim = t.Turtle()

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range (3, 11):
#     tim.color(random.choice(color_list))
#     draw_shape(shape_side_n)


#random walk
#tap into module to change the color mode to 255 rgb scale
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

mover = t.Turtle()
headings = [0, 90, 180, 270]
mover.width(10)
mover.speed(10)

#random walk
# for _ in range(500):
#     mover.color(random_color())
#     mover.forward(30)
#     mover.setheading(random.choice(headings))

#spirograph
spiro = t.Turtle()
spiro.speed("fastest")

def draw_spirograph(offset_angle):
    for n in range(int(360 / offset_angle)):
        spiro.color(random_color())
        spiro.circle(100)
        spiro.setheading(spiro.heading()+offset_angle)

draw_spirograph(1)


screen = t.Screen()
screen.exitonclick()