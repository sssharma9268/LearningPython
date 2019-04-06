class Person:
    """Shows information of a person"""
    location = "INDIA"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def displayPerson(self):
        print("Name:{0} Age:{1} Location:{2}".format(self.name,self.age,Person.location))


p1 = Person("Sumit",25)
p1.displayPerson()
p1.name = "Sharma "
print(p1.name)
print(p1.age)
print(getattr(p1,'age'))
print(setattr(p1,'age',30))
p1.displayPerson()
#delattr(p1,'age')