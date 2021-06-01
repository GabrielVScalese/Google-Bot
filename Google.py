import requests
import os
import json
import datetime
from pytz import timezone
from Answer import Answer

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')
CSE = os.getenv('CSE')

class Google:

  @staticmethod
  def get_news_from_now_time (news, now_time, period):
    ret = []

    for new in news:
      date_time_str = new['publishedAt']

      date_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S%z')

      new_date_time = date_time.astimezone(timezone('America/Sao_Paulo'))

      one_time = datetime.timedelta(hours=period)

      if (new_date_time > now_time - one_time):
          ret.append(new)
      
    return ret

  @staticmethod
  def get_news (now_time, country):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'

    response = requests.get(url)

    news = response.json()['articles']

    return Google.get_news_from_now_time(news, now_time, 1)

  @staticmethod
  def get_new_from_name (name):
    url = ('https://newsapi.org/v2/everything?'
       f'q={name}&'
       'language=pt&'
       f'apiKey={NEWS_API_KEY}')

    response = requests.get(url)

    news = response.json()['articles']

    return news
  
  @staticmethod
  def get_answers (search, num):
    answers = []

    try:
      url = f'https://www.googleapis.com/customsearch/v1?key={DEVELOPER_KEY}&cx={CSE}&cr=countryBR&gl=br&lr=lang_pt&q={search}&num={num}'

      data = requests.get(url).json()
      search_items = data.get('items')
      
      for i, search_item in enumerate(search_items, start=1):
        answer = Answer(search_item.get('title'), search_item.get('link'), search_item.get('displayLink'), search_item.get('snippet'))

        answers.append(answer)
      
      return answers
    except:
        return answers
  
  @staticmethod
  def get_images (search, num):
    images = []

    try:
      url = f'https://www.googleapis.com/customsearch/v1?key={DEVELOPER_KEY}&cx={CSE}&cr=countryBR&gl=br&lr=lang_pt&q={search}&searchType=image&num={num}'

      print(url)

      data = requests.get(url).json()
      search_items = data.get('items')
      
      for i, search_item in enumerate(search_items, start=1):
        images.append(search_item.get('link'))

      return images
    except:
      return images
    




  