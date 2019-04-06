class Horse:
    def run(self):
        print("Horse can run fast")

    def domesticated(self):
        print("Horses can be domesticated")

class Zebra:
    def run(self):
        print("Zebra can run fast")

    def domesticated(self):
        print("Zebra can not be domesticated")

def live_with_people(animal):
    animal.domesticated()

h = Horse()
z = Zebra()

live_with_people(h)
live_with_people(z)

for animal in (h,z):
    animal.run()
    animal.domesticated()