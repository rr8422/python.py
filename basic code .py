# This is a comment in Python
# Comments are used to provide explanations or document the code

# Printing a message to the console
print("Hello, world!")

# Variables and data types
name = "Alice"  # String variable
age = 25        # Integer variable
height = 1.75   # Float variable
is_student = True   # Boolean variable

# Conditional statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Looping
for i in range(5):
    print(i)

# Functions
def greet_person(name):
    print("Hello, " + name + "!")

greet_person("Bob")

# Lists
fruits = ["apple", "banana", "orange"]
print(fruits[0])    # Accessing the first element of the list
fruits.append("grape")   # Adding an element to the list
print(len(fruits))  # Getting the length of the list

# Dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person["name"])   # Accessing the value by key
person["age"] += 1      # Modifying the value

# Classes
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())
