from turtle import Turtle
BALL_SPEED = 0.01

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.x_speed = 3  #can adjust ball speed here or at screen.sleep in main file
        self.y_speed = 3
        self.ball_speed = BALL_SPEED #set the starting ball speed

    def move(self):
        new_x = self.xcor()+ self.x_speed
        new_y = self.ycor()+ self.y_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
        self.ball_speed *= 0.5 #reduces the pause of the game so that the ball speed increases each time a paddle hits it

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x() # reverse the direction of the ball
        self.ball_speed = BALL_SPEED