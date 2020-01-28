import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://www.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok?pmax=25000'
page_part = '&p='


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def get_page_data(html):
    total_data = []
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='item_table')
    for ad in ads:
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = 'none'
        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = 'none'
        try:
            price = ad.find('div', class_='about').text.split('₽')[0].strip()
        except:
            price = 'none'
        try:
            metro = ad.find('span', class_='item-address-georeferences-item__content').text.strip()
        except:
            metro = 'none'
        data = {'type': title.split(',')[0],
                'area': title.split(',')[1][1:3],
                'url': url,
                'price': price,
                'metro': metro
                }
        total_data.append(data)
    return total_data


def json_export(data):
    with open('hati.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)


def main():
    total_pages = get_total_pages(get_html(base_url))
    pages_data = []
    for i in range(1, total_pages + 1):
        url_gen = base_url + page_part + str(i)
        html = get_html(url_gen)
        page_data = get_page_data(html)
        for flat in page_data:
            pages_data.append(flat)
        print(i)
    json_export(pages_data)

    print(get_total_pages(get_html(base_url)))


if __name__ == '__main__':
    main()
