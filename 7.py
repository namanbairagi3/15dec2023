# class Defination 
class Bike():# ClassName always be in PascalCase 
    #1 Property
    company =''
    model =''

    #2 Constructor
    def __init__(self, company, model): #always put first arguement as self
        self.company = company
        self.model = model

    #3 Method
    def display_info(self):
        print(f"{self.company} {self.model}") #always put first arguement as self

# Creating an instance of the Car class
Bike1 = Bike(company="Hero", model="HF Delux")
Bike1.display_info()
