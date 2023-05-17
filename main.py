import time
# print("I love pizza ")
# print("Shut the fuck up")
# name = "Ndulue Vera "
# print(name)
# x = 123
# print(x)
# print("hello " + name)
# print(name + str(x))

# Quality, name, sex = 12, "Vera",  "female"
# print(Quality)
# print(name)
# print(sex)
# Patrick = Phyll = Wisdom = 20
# print(Patrick)
# print(Phyll)
# print(Wisdom)
# # Typecasting
# x = 12
# y =20.9
# z = "Hello"
# print(int(y))
# # User input
# name = input("What is your name?")
# print("Hello " + name)
# age = int(input("How old are you?"))
# print("you are " + str(age) + " years old")

# import math
# pi = 3.14
# print(math.ceil(pi))
# age = int(input("How old are you?"))
# if age >= 18 :
#     print("You are an adult")
# elif age < 0 :
#     print("You are not born yet")
# elif age == 100 :
#     print("You are very old")
# else:

#     print("You are still a kid")

# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("Hello " + name)
#
# for i in range(10):
#     print(i + 1)
#
# for i in range(50, 100 + 1, 2):
#     print(i)

# for i in "Ndulue Vera":
#     print(i)
#
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year")

# rows = int(input("How many rows? :"))
# Columns = int(input("How many Columns? :"))
# Symbol = input("What symbol do you want? :")
#
# for i in range(rows):
#     for i in range(Columns) :
#         print(Symbol, end="")
#     print()
#     break
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break
#
# # Continue
# phone_number = "123-456-789"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end=" ")
# # pass
# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)
# List
food = ["pizza", "tomato", "Hamburger", "spaghetti", "pudding"]
food[0] = "sushi"
# print(food[0])
food.append("cake")
food.append("Ice cream")
for x in food:
    print(x, end=" ")

# 2d list
drinks = ["coffee","soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
desert = ["cake", "ice cream"]

foods = [drinks, dinner, desert]
print (foods)
print(foods[1][2])


# tuple

student = ("Vera", 21, "female")
print(student.count("vera"))
print(student.index("female"))

for x in student:
    print(x)
if "vera" in student:
    print("Vera is here ")

    # Sets

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plates", "cup"}

# utensils.add("napkin")
# utensils.remove("spoon")
utensils.update(dishes)
for x in utensils:
    print(x)

# dictionary

capitals = {"USA":"Washington DC", "India":"New Dehli",
            "China":"Beijing",
            "Russian":"Moscow"}
capitals.update({"Germany":"Berlin"})
# print(capitals["Russian"])
# print(capitals.keys())
print(capitals.items())
for key,value in capitals.items():
    print(key,value)

# Function in python
def hello(first_name, second_name, age):
    print("Hello " + first_name + "  " + second_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day")
hello("Vera", "Ndulue",21)
hello("Phyll", "Ndulue",20)
hello("Wisdom","Ahuzi", 19)

# return statement
def multiply(number1, number2):
    result = number1 * number2
    return result
x = multiply(6,8)
print(x)

