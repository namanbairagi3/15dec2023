class Person:
    #Property

    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Method
    def myName(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
co = Person(name="naman", age=22)


# Accessing attributes and calling methods
print(f"{co.name} is {co.age} years old.")
co.myName()
