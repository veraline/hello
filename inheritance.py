# Inheritance
class Person:
    def __init__(self, fname, lname, graduationyear):
        self.firstname = fname
        self.lastname = lname
        self.graduate = graduationyear

    def printname(self):
        print(self.firstname, self.lastname, self.graduate)

# x = Person("Vera", "Ndulue")
# x.printname()


class Student(Person):
    def __int__(self, fname, lname, graduationyear):
        # Person.__init__(self, fname, lname)
        super().__init__(self, fname, lname, graduationyear)


x = Student("Mike", "Olsen", 2019)
x.printname()