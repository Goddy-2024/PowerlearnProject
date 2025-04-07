"""Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values."""
class Smartphone:
    def __init__(self, color, make, price):
        self.color = color
        self.make = make
        self.price = price

class Book:
    def __init__(self, pages, author, genre):
        self.pages = pages
        self.author = author
        self.genre = genre

class Superhero:
    def __init__(self, name_):
        self.name_ = name_

MySamsung = Smartphone("black", "Samsung", "19000 KES")
CarriesIphone = Smartphone("black", "iPhone", "91000 KES")

# Output
print(f"People live similar and different lives lol 😂")
print(f"Carrie and I both have {MySamsung.color} smartphones.")
print(f"Carrie has a {CarriesIphone.color} {CarriesIphone.make} while I have a {MySamsung.color} {MySamsung.make}.")
print("See, life is the same and different at the same time 😂")

"""
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️)."""
class Animal:
    def move(self):
        print("This animal moves the way it was created")

class Dog(Animal):
    def move(self):
        print("A Dog runs")

class Fish(Animal):
    def move(self):
        print("A Fish swims")

class Bird(Animal):
    def move(self):
        print("A Bird flies")

class Vehicle:
    def move(self):
        print("A vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("A Car drives")

class Plane(Vehicle):
    def move(self):
        print("A Plane flies")

objects = [Dog(), Fish(), Bird(), Car(), Plane()]

for item in objects:
    item.move()
