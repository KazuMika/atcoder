import requests
from bs4 import BeautifulSoup

def beau_practice():
    res = requests.get('http://quotes.toscrape.com/')
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def get_piyo_text(soup):
    print(soup)
    piyo = soup.select_one('div.hoge div.fuga div.piyo')
    if not piyo:
        return None
    return piyo.get_text()


soup= beau_practice()
piyo = get_piyo_text(soup)
print(piyo)
