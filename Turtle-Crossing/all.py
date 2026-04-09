from turtle import Turtle
import random
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 16, "bold")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.go_to_start()
        # self.next_level()

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() -MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)



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



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align= "left", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font= FONT )

