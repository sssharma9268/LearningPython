#encapsulation is an internal representation of an object
#and it is hidden for other objects. It can be used to hide variables and methods
#they can only be accessible in an object

class Bear:
    __maxSpeed = 35 #here double underscore means it is private

    def __init__(self,name):
        self.name = name

    def run(self):
        print("{} bear can run {} km/hr".format(self.name,self.__maxSpeed))

    def setmaxSpeed(self,newSpeed):
        self.__maxSpeed = newSpeed

grizzly = Bear("Grizzly")
grizzly.setmaxSpeed(56)
grizzly.run()
#print(grizzly.__maxSpeed) #here maxSpeed private variable is not directly accessible to instance. it can only be accessed by its own methods
#The values of private variables cannot be changed directly, you will have to define a method to update the private variable


