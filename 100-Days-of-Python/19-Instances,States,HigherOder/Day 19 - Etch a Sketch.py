from turtle import Turtle, Screen

es = Turtle()
screen = Screen()

def move_forward():
    es.forward(10)

def move_backward():
    es.backward(10)

def turn_left():
    es_heading = es.heading() + 10
    es.setheading(es_heading)

def turn_right():
    es_heading = es.heading() - 10
    es.setheading(es_heading)


# start listening for events
screen.listen()

# have to use a function that will be triggered; bind a keystroke --> use an 'event listener'
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=es.reset)


screen.exitonclick()