# class Defination   
class Country:# ClassName always be in PascalCase 
    #1 Property
    name =''
    population =""
    capital = ''

     #2 Constructor
    def __init__(self, name, population, capital): #always put first arguement as self
        self.name = name
        self.population = population
        self.capital = capital

    #Method
    def show_info(self):
        print(f"{self.name} population is {self.population} and  capital of india is {self.capital}.") #always put first arguement as self

# Creating an instance of the Country class
country1 = Country(name="India", population=1425775850, capital="Delhi")
country1.show_info()
