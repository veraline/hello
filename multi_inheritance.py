# multil-level inhertance, a class inheriting from another class

class Organism:
    alive = True


class Animal(Organism):
    def eat(self):
        print("This animal is eating")


class Dog(Animal):
    def bark(self):
        print("This Dog is barking")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()