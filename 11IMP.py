class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Creating an instance of the Person class
person2 = Person(name="Bob", age=30)
person2.celebrate_birthday()
