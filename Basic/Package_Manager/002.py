import requests
from bs4 import BeautifulSoup
r = requests.get('https://codingeverybody.github.io/scraping_sample/1.html')
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title.string)

emClass = soup.findAll('div', {'class' : 'em'})
print(emClass)
