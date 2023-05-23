# Object-oriented programing in python
class Myclass:
    x = 5


p1 = Myclass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p2 = Person("John", 26)
print(p2.name)
print(p2.age)

# The __Str__() Function


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p3 = Person2("Vera", 34)
print(p3.name)
print(p3.age)


# objects methods
class Person4:
    def __init__(self, name, age, Nationality):
        self.name = name
        self.age = age
        self.Nationality = Nationality

    def myfunc(self):
        print("Hello my name is " + self.name + " I am " + str(self.age) + " Years old")
        print("I am from " + self.Nationality)


p4 = Person4("Wisdom", 190, "Nigerian")
p4.myfunc()


# Pass statement
class Book:
    pass

