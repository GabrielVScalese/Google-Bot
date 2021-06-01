class Vaccine:

  def __init__(self, country, capital, continent, population, vaccinated, partially_vaccinated, updated):
    self.country = country
    self.capital = capital
    self.continent = continent
    self.population = population
    self.vaccinated = vaccinated
    self.partially_vaccinated = partially_vaccinated
    self.updated = updated

  def to_string(self):
    return f'Country: {self.country} | Capital: {self.capital} | Continent: {self.continent} | Population: {self.population} | Vaccinated: {self.vaccinated} | Partially vaccinated: {self.partially_vaccinated} | Updated: {self.updated}' 
