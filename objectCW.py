#
# Start with a main function and make each problem a function. Call those functions from your main function.
#
# Problem 1:
#
# Create a class Dog. Make sure it has the attributes name, breed, color, gender. Create a function that will print all attributes of the class. Create an object of Dog in your problem1 function and print all of it's attributes.
#
class Dog:
    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender

    def printAttr(self):
        print(f'This dog is {self.name}, {self.breed}, {self.color}, and {self.gender}.')


def problem1():
    option1 = Dog("Bruno", "Pitbull", "Blue", "Male")
    option1.printAttr()


problem1()


# Problem 2:
#
# We will keep having this problem until EVERYONE gets it right without help
#
# Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.

def problem2():
    userInput = ""
    while (userInput != 'q'):
        userInput = input("Enter another string:  ")


problem2()


# Problem 3:
#
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
# The class should have several functions:
# a) One function that can change the name of the product.
# b) Another function that can change the name and price of the product.
# c) A last function that can change the name, price, and quantity of the product.
# Create an object of Product and print all of it's attributes.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def changeName(self, newName):
        self.name = newName
        return newName

    def changeNamePrice(self, newnewName, newPrice):
        self.name = newnewName
        self.price = newPrice
        return newnewName, newPrice

    def changeAll(self, newnewnewName, newnewPrice, newQuan):
        self.name = newnewnewName
        self.price = newnewPrice
        self.quantity = newQuan
        return newnewnewName, newnewPrice, newQuan

def problem3():
    option1 = Product("Big Burgers", "$10", 50)
    print(option1.name, option1.price, option1.quantity)

problem3()