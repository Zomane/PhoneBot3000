import re
import colored
import requests
import termcolor
from bs4 import BeautifulSoup
import json

def get_product_links():
    pages = ["https://betaren.ru/catalog/semena/drazhirovannye-semena-sakharnoy-svekly/?PAGEN_1=1",
             "https://betaren.ru/catalog/semena/drazhirovannye-semena-sakharnoy-svekly/?PAGEN_1=2",
             "https://betaren.ru/catalog/semena/semena-ozimoy-pshenitsy/",
             "https://betaren.ru/catalog/semena/semena-yarovoy-pshenitsy/",
             "https://betaren.ru/catalog/semena/semena-soi/",
             "https://betaren.ru/catalog/semena/semena-zernobobovykh-kultur/",
             "https://betaren.ru/catalog/semena/semena-podsolnechnika/",
             "https://betaren.ru/catalog/semena/semena-kukuruzy/",
             "https://betaren.ru/catalog/semena/semena-rapsa/"]
    product_links = []
    for i in range(len(pages)):
        print(i)
        req = requests.get(pages[i])
        soup = BeautifulSoup(str(BeautifulSoup(req.text, 'html.parser').find_all('div', class_='preview-image')),
                             'html.parser')

        for link in soup.find_all('a'):
            product_links.append("https://betaren.ru" + link.get('href'))
        print(len(product_links))

    return product_links


def write_product_info(links):
    for link in links:
        req = requests.get(link).text
        soup = BeautifulSoup(req, 'html.parser')
        data = []
        name = soup.find('div', class_='catalog-element-card__title-wrapper').find('h1').text

        # data.append(soup.find("tbody").text)
        # print(data)

        table_data = [[cell.text for cell in row("td")]for row in BeautifulSoup(req, features="html.parser")("tr")]

        with open(f'data/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(table_data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    links = get_product_links()
    write_product_info(links)