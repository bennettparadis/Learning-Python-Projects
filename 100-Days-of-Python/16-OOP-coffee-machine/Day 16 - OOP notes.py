# #import a module
# #import turtle 

# #tap into the turtle module, call the class to assign it to a new object of class Turtle
# #timmy = turtle.Turtle()

# #alternatively
# from turtle import Turtle, Screen

# timmy = Turtle()

# #functions tied to an object
# #car.stop() --> calling the function associated with the object
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(200)

# #attributes
# #variables assigned to an object of that class
# # ex. car.speed --> speed of the car object

# #create a screen object called my_screen
# my_screen = Screen()
# #take a look at one of the attributes of screen object, canv height --> print out a value for the dimension of my_screen, 300
# print(my_screen.canvheight)

# #this line basically needs to be last
# my_screen.exitonclick()


####Installing and using Packages 
#past exercises used modules that were other files. A package is a lot of code, lots of files others have writeen packaged together for a specific purpose
#search for packages @ pypi.org ---> pythong package index

# to install a package in VSCode, open terminal and type: py -m pip install [name of package]
from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ['Electric', 'Water','Fire'])
print(table)



