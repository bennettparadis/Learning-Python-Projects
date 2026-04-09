import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# START listening for keystrokes as input
screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1) #screen refreshes every 0.1s
    screen.update()

    #each time the screen refreshes, a new car is created and all the cars move
    #this would be a lot of cars, hence the random chance line in the car_manager file
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) <20:
            game_is_on = False
            scoreboard.game_over()

    # Detect finish line crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.add_speed()
        scoreboard.next_level()

screen.exitonclick()
