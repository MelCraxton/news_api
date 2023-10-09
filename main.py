#  Use requests when you want to browse an api
import requests

#  https://newsapi.org/
api_key = '58df71ff4ef1421893045a627b52d7db'

#  This is the endpoint
url = 'https://newsapi.org/v2/everything?q=tesla&'\
    'from=2023-09-09&sortBy=publishedAt&'\
    'apiKey=58df71ff4ef1421893045a627b52d7db'

#  Make a request
request = requests.get(url)
# The above url returns a string - print(type(content))
# use .json to convert it to a dict
content = request.json()

# Access the article title and description
for article in content['articles']:
    print(article['title'])
    print(article['author'])