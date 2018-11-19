# # a class is a recipe
# # an object is the food you mde with recipe
# # the recipe can be used lots and lots of times
# # Classes are capitalized 

# # class first then objects created based off class. You can modify object info
# # can create multiple objects with same starting information

# class Car(object):
#     # whenever we start making a new car, __init__ will run
#     # we always pass self first
#     def __init__(self):
#         # self is special
#         # self refers to THIS object
#         self.make = "Honda"
#         self.model = "Accord"
#         self.year = 2007

# #myCar and yourCar are objects
# myCar = Car()
# print myCar.make
# yourCar = Car()
# print yourCar.make
# yourCar.make = "Toyota"
# print yourCar.make

class Car(object):
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def changeModel(self,newModel):
        self.model = newModel

zachsCar = Car("Ford","F150")
chrisCar = Car("Chevrolet", "Silverado")
zachsCar.isCool = "Awesome"
print zachsCar.make
print chrisCar.make
print zachsCar.model
print chrisCar.model
print zachsCar.isCool

zachsCar.model = "Focus"
# ZACHS CAR: DON'T MESS WITH ME
print zachsCar.model
# using different function in class
zachsCar.changeModel("Fiesta")
# NO DIFFWRENCE BETWEEN THESE TWO WAYS IN TERMS OF RESULTS
zachsCar.model = "Fiesta"
print zachsCar.model