class Cases:

  def __init__(self, country, flag, capital, continent, population, confirmed, recovered, deaths, life_expectancy, updated):
    self.country = country
    self.flag = flag
    self.capital = capital
    self.continent = continent
    self.population = population
    self.confirmed = confirmed
    self.recovered = recovered
    self.deaths = deaths
    self.life_expectancy = life_expectancy
    self.updated = updated

  def get_country(self):
    return self.country
  
  def get_flag(self):
    return self.flag
  
  def get_capital (self):
    return self.capital
  
  def get_continent (self):
    return self.continent
  
  def get_population (self):
    return self.population
  
  def get_confirmed (self):
    return self.confirmed
  
  def get_recovered (self):
    return self.recovered
  
  def get_deaths (self):
    return self.deaths
  
  def get_life_expectancy (self):
    return self.life_expectancy
  
  def get_updated (self):
    return self.updated
  
  def to_string(self):
    return f'Country: {self.country} | Capital: {self.capital} | Continent: {self.continent} | Population: {self.population} | Confirmed: {self.confirmed} | Recovered: {self.recovered} | Deaths: {self.deaths} | Life expectancy: {self.life_expectancy} | Updated: {self.updated}'