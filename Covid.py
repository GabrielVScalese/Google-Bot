import requests
from Cases import Cases
from Vaccine import Vaccine

class Covid:

  @staticmethod
  def get_cases (country):
    try:
      url = (f'https://covid-api.mmediagroup.fr/v1/cases?country={country}')

      response = requests.get(url)
      data = response.json()['All']

      country_url = f'https://restcountries.eu/rest/v2/name/{country}'

      response = requests.get(country_url)
      alpha_code =  response.json()[0]['alpha2Code']

      flag_url = f'http://www.geognos.com/api/en/countries/flag/{alpha_code}.png'

      try:
        updated = data['updated']
      except:
        updated = ""

      cases = Cases(data['country'], flag_url, data['capital_city'], data['continent'], data['population'], data['confirmed'], data['recovered'], data['deaths'], data['life_expectancy'], updated)

      return cases
    except:
      return None
  
  @staticmethod
  def get_vaccine (country):
    url = (f'https://covid-api.mmediagroup.fr/v1/vaccines?country={country}')

    response = requests.get(url)

    data = response.json()['All']
    vaccine = Vaccine(data['country'], data['capital_city'], data['continent'], data['population'], data['people_vaccinated'], data['people_partially_vaccinated'], data['updated'])

    return vaccine.to_string()


