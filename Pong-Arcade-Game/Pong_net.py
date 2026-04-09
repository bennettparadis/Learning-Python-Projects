from turtle import Turtle

class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 290)
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.width(5)
        self.draw_net()

    def draw_net(self):
        for distance in range(0, 15):
            self.setheading(270)
            self.penup()
            self.forward(25)
            self.pendown()
            self.forward(25)

