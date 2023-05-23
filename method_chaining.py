#method chaining

class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You turn off the Car")
        return self


car = Car()
#method chaining
car.brake().turn_off().drive().turn_on()
