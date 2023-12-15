class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, I'm {self.name}, and I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person(name="Alice", age=25)
person1.introduce()
