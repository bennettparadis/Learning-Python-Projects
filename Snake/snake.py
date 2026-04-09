from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # when a new snake is created, these attributes are set with it - snake body, perform create snake func, and snake's head
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_block = Turtle(shape="square")
        new_block.color('white')
        new_block.penup()
        new_block.goto(position)
        self.snake_body.append(new_block)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())


    def move(self):
        # for correct movement of snake segments, actually need to go in reverse order --> ex./ the third piece moves to where the second piece is, then the second piece moves to where the first piece is, and the first piece moves forward
        for segment_number in range(len(self.snake_body ) -1 , 0, -1):  # start, stop, step
            # get position of the segment ahead of the current step
            new_x = self.snake_body[segment_number -1].xcor()
            new_y = self.snake_body[segment_number - 1].ycor()
            # move the current iterable segment to the position of the next segment
            self.snake_body[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    # movement functions
    def up(self):
        # if current heading is pointed down, snake cant move up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]