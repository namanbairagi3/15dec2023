
class A:

    # 1. Property
    name = ""
    surname = ""

    # 2. Constructor
    def __init__(self, a, b):  # always put the first argument as self
        # Constructor initializes the property
        self.name = a
        self.surname = b
        
    # 3. Method
    def add(self):  # always put the first argument as self
        print(f"My Name is {self.name} {self.surname}")

co = A("abhishek", "bairagi")
co.add()
