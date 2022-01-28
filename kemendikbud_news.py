import requests
from bs4 import BeautifulSoup

url ='https://www.kemdikbud.go.id/main/blog/category/berita'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

res = requests.get(url, headers=headers)
#print(res.status_code)
# if status code is 200, then you can scrape the news title from that url

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())

titles = soup.findAll('article', 'single_post')

for title in titles:
    judul = title.find('strong').text
    print(judul)
