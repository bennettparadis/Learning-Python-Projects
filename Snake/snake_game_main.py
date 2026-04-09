from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(height= 600, width=600)
screen.bgcolor('black')
screen.title("Classic Snake")
#setting up the animation with tracer
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
#START listening for keystrokes as input
screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")

# move snake to automatically move forward
game_is_on = True
while game_is_on:
    #call screen update so that the screen is updated, or a new frame is created, once the loop has gone through
    #update the screen once all the segments move forward; then the update is triggered and graphics refreshed
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()
        print("nom nom nom")

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if head collides with any segment in the body or tail
    for segment in snake.snake_body[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()






screen.exitonclick()
