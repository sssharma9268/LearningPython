class Animal:
    def swim(self):
        print("Animals can swim")

class Tiger(Animal):

    def swim(self):
        print("Tigers can swim")

tiger = Tiger()
tiger.swim()