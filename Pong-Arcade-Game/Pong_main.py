from turtle import Turtle, Screen
from Pong_net import Net
from Pong_paddles import Paddle
from Pong_ball import Ball
from Pong_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title("Classic Pong")
# setting up the animation with tracer
screen.tracer(0) # turns off the animation, but need to a refresher with while loop

p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))
ball = Ball()
net = Net()
scoreboard = Scoreboard()

# START listening for keystrokes as input
screen.listen()
screen.onkeypress(p1.go_up, "w")
screen.onkeypress(p1.go_down, "s")
screen.onkeypress(p2.go_up, "Up")
screen.onkeypress(p2.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed) # pauses the while loop and screen update, slows ball movement
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(p2) < 40 and ball.xcor() > 335 and ball.x_speed > 0 or ball.distance(p1) < 40 and ball.xcor() < -335 and ball.x_speed < 0:
        ball.bounce_x()

    # Detect miss by p1, add score to p2
    if ball.xcor() < -380:
        time.sleep(1)
        scoreboard.p2_point()
        ball.reset_position()

    # Detect miss by p2, add score to p1
    if ball.xcor() >380:
        time.sleep(1)
        scoreboard.p1_point()
        ball.reset_position()



screen.exitonclick()
