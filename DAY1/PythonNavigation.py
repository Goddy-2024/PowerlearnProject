"""A programing language that is usedin software development with the advanced features as it is:
SIMPLE
HIGH LEVEL
INTERPRETED
OBJECT ORIENTED 
OPEN SOURCE
GUI PROGRAMING
LARGE STABDARD LIBRARY
EXPRESSIVE LANGUAGE
 like in other programming languages python has the following features:
variables(Data Stores)
Control Flow(Decosion Making Elements)
Loops(Repeating Tasks)
Other Data Sturctures"""

#LTSTS- used  to store multiple data at once
#A list of three numbers
numbers = [1,2,3]
print(numbers)
#the data in lists may be of different types
my_list = ["Godswill", 19, "BSE S/W ENGINEERING", "MULTIMEDIA UNIVERSITY OF KENYA"]
print(my_list)
#lists supports indexing
print(f"my name is {my_list[0]}, I'm age {my_list[1]}, currently studying {my_list[2]} in the {my_list[3]}")
#slicing lists
my_languages = ["Javascript", "CSS", "HTML5", "python", "C", "Java", "C++"]
print(f"I am a WEB developer proficient in {my_languages[0:3]} and {my_languages[3:4]}, I have a glitch also in {my_languages[4:5]} and abit of {my_languages[5:]} and so in aggreagate im good in {my_languages[:]}")
#Adding Elements to a Python list:
#1) Using the .append() method - adds an item at the end of the list
#the parameter here si the item to be added, and has no return value
my_languages.append("R")#adds R at the end omf my_languages list
print(my_languages)
#2)Using the .extend() method - used to add all items of one list to another
other_languages = ["Rust", "C#", "DART", "JSON", "JSX", "TypeScript"]
# regarding parameters and return values, .extend() method works the same way as .append()
other_languages.extend(my_languages)
print(other_languages)
##since python lists are mutable we can change the items by assigning new items to the position of the existing items
numbers[0] = "one"
numbers[1] = "Two"
numbers[2] = "Three"
print(numbers)
#mutability using del statement
del numbers[2]
print(numbers)
#mutability using the .remove() method
numbers.remove("one")
print(numbers)#['Two']



#DICTIONARIES
capital_cities = {
    "Kenya":"Nairobi",
    "Nigeria":"Abuja",
    "Uganda":"Kampala",
    "Tanzania":"Dar_Es_Saalam"
}
#Accessing dictionaries
print(f"The capital City of Kenya is {capital_cities['Kenya']}")

#SETS
account_names = {"John", "Jane", "Alice", "Bob", "Mary"}
account_names = {"John", "Jane", "Alice", "John", "Mary"}#Allows you to avoid duplication of values
print(account_names)
print(account_names.pop())

#PYTHON CONDITIONAL STATEMENTS
def stud_grading(marks):

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "pass"
    return grade 
print(stud_grading(99))
