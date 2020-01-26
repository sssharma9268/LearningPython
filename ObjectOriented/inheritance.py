class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def test(self):
        print("Test Statement")

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def test2(self):
        print("Test Statement of class Student")

#multiple inheritance, priority is given from left to right when attributes or methods of two base classes are same.
class Employee(Person,Student):
    def displayInfo(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

e = Employee("Sumit",25)
e.displayInfo()
e.test2()