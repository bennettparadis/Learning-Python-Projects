# Classes can inherit or pass on attributes and methods
class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# Animal class is parent class
class Fish(Animal):
    #initialize
    def __init__(self):
        #initialize everything the parent class, or super-class, can do as well
        # this line inherits everything from superclass Animal
        super().__init__()

    def swim(self):
        print("Just keep swimming...")

    # can modify methods from superclass, add something specific; add functionality
    def breathe(self):
        super().breathe()
        print("doing this underwater")
    # now, when calling the breathe function for a fish object, it will do both
    # so the Animal breathe function occurs, as does the subclass function

nemo = Fish()

nemo.breathe()