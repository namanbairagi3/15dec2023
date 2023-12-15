# class Defination 
class Student:# ClassName always be in PascalCase 
     #1 Property
    name =''
    grade =''
     #2 Constructor
    def __init__(self, name, grade): #always put first arguement as self
        self.name = name
        self.grade = grade

    #3Method
    def promote(self):
        self.grade += 1
        print(f"{self.name} has been promoted to grade {self.grade}.") #always put first arguement as self

# Creating an instance of the Student class
student1 = Student(name="sonu", grade=11)
student1.promote()
