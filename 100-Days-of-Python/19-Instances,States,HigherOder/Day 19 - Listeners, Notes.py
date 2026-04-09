from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

# start listening for events
screen.listen()

# have to use a function that will be triggered; bind a keystroke --> use an 'event listener'
screen.onkey(key="space", fun=move_forward) # method does not have parentheses --> parenthese tell method to execute
# the line above passes the function into another function --> higher order function
# in the case above, onkey() is a higher order function
# very good practice to include keywords in arguments, rather than positional

screen.exitonclick()





# Objects, instances, and state
# timmy is an object of class Turtle
# can create multiple turtle objects
# functions of objects may be completely different/independent of one another;
# these would be multiple 'instances' of class Turtle
# two turtles could have colors/attributes or different methods at any one times --> their 'state'
# different state in attributes or different state in function of methods

