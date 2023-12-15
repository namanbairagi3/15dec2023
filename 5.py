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
person1 = Person(name="naman", age=22)


# Accessing attributes and calling methods
print(f"{person1.name} is {person1.age} years old.")
person1.myName()
