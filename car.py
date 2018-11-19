# a class is a recipe
# an object is the food you mde with recipe
# the recipe can be used lots and lots of times
# Classes are capitalized 

class Car(object):
    # whenever we start making a new car, __init__ will run
    # we always pass self first
    def __init__(self):
        # self is special
        # self refers to THIS object
        self.make = "Honda"
        self.model = "Accord"
        self.year = 2007

myCar = Car()