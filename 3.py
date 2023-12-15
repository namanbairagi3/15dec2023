class Dog():
    #1 Property
    species = "Canis familiaris"

    #2 Constructor 
    def __init__(self, name, age):#always put first arguement as self
        # Instance attributes
        self.name = name
        self.age = age

    #3 Method
    def bark(self):
        print(f"{self.name} says Woof!")#always put first arguement as self

# Creating an instance of the Dog class
my_dog = Dog(name="Lucy", age="1 Month")

# Accessing attributes and calling methods
print(f"{my_dog.name} is a {my_dog.age}-Month-old {my_dog.species}.")
my_dog.bark()
