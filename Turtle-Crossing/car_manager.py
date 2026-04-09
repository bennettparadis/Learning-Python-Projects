from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager(Turtle):
    def __init__(self):
        # empty list of cars
        super().__init__()
        self.all_cars = []
        # empty list of speeds --> used for variable car speeds between levels
        self.speeds = [STARTING_MOVE_DISTANCE]

    def create_car(self):
        random_chance = random.randint(1,6)
        #adjust the length of the random chance list to adjust frequency of new cars being generated
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1 , stretch_len= 2)
            new_car.penup()
            new_car.speed = random.choice(self.speeds) # assign a random speed to each car
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(car.speed)

    def add_speed(self):
        # make a new max speed for each new level
        new_speed = max(self.speeds) + MOVE_INCREMENT
        # list of speeds is updated
        self.speeds.append(new_speed)


