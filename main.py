from send_email import send_email

#  Use requests when you want to browse an api
import requests

#  https://newsapi.org/
api_key = '58df71ff4ef1421893045a627b52d7db'

topic = 'tesla'

#  This is the endpoint
url = f'https://newsapi.org/v2/everything?q={topic}&' \
      'from=2023-09-11&sortBy=publishedAt&' \
      'apiKey=58df71ff4ef1421893045a627b52d7db&' \
      'language=en'

#  Make a request
request = requests.get(url)
# The above url returns a string - print(type(content))

# use .json to convert it to a dict
content = request.json()
print(content)
# Access the article title and description
body = ''
for article in content['articles'][0:20]:
    # print(article['title'])
    # print(article['author'])
    if article['title'] is not None:
        body = "Subject: Today's news" + '\n' \
               + body + article['title'] + "\n" \
               + article['publishedAt'] + "\n"  \
               + article['url'] \
               + '\n' + 2 * '\n'

body = body.encode('utf-8')
send_email(message=body)
