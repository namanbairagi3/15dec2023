class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show_info(self):
        print(f"{self.name} has a population of {self.population} and its capital is {self.capital}.")

# Creating an instance of the Country class
country1 = Country(name="Canada", population=38000000, capital="Ottawa")
country1.show_info()
