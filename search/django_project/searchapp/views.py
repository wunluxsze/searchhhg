from locale import currency
from this import d
from django.shortcuts import render
from searchapp import func
import requests
from dataclasses import dataclass
from urllib.parse import urljoin
from typing import List

from bs4 import BeautifulSoup

def parse_currency():
    DOLLAR_URL = 'https://finance.rambler.ru/currencies/USD'
    dollar_response = requests.get(DOLLAR_URL)
    dollar_parser = BeautifulSoup(dollar_response.text, 'html.parser')
    dollar_currency_item = dollar_parser.find('div', 'finance-currency-plate__currency').text.strip()
    dollar_string = '1 $ = ' + str(round(float(dollar_currency_item), 2)) + ' ₽'
    
    EURO_URL = 'https://finance.rambler.ru/currencies/EUR'
    euro_response = requests.get(EURO_URL)
    euro_parser = BeautifulSoup(euro_response.text, 'html.parser')
    euro_currency_item = euro_parser.find('div', 'finance-currency-plate__currency').text.strip()
    euro_string = '1 € = ' + str(round(float(euro_currency_item), 2)) + ' ₽'
    return [dollar_string, euro_string]



@dataclass
class Anime:
    url: str
    title: str


session = requests.session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'


def search(text: str) -> List[Anime]:
    data = {
        'ajax_load': 'yes',
        'start_from_page': 1,
        'show_search': text,
        'anime_of_user': '',
    }
    headers = {
        'X-Requested-With': 'XMLHttpRequest',  # AJAX
    }
    rs = session.post('https://jut.su/anime/', headers=headers, data=data)
    rs.raise_for_status()

    items = []
    root = BeautifulSoup(rs.text, 'html.parser')
    for anime_el in root.select('.all_anime_global'):
        url = urljoin(rs.url, anime_el.a['href'])
        title = anime_el.select_one('.aaname').text

        items.append(Anime(url, title))

    return items





def search_sentence(request): #функция для отправки списка в html
    search_check = False
    [dollar, euro] = parse_currency()
    if 'q' in request.GET and request.GET["q"] != '':
        search_check = True
        result = search(request.GET["q"])
        result = [f"<a class='anime__href' href='{i.url}'>{i.title}</a>" for i in result]
        return render(request, 'index.html', context={"sentences": result, 'check': search_check, "dollar": dollar, "euro": euro }) #отправка списка и переменную которая проверяет есть ли запрос
    return render(request, 'index.html', {"dollar": dollar, "euro": euro})  #если пустое то обновляется страница


    