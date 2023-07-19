import re
import colored
import requests
import termcolor
from bs4 import BeautifulSoup


def write_product_info(links_of_products):
    print(links_of_products)
    for link in links_of_products:
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')
        name = soup.find('div', class_='catalog-element-card__title-wrapper').find('h1').text
        product_type = ''
        compound = ''
        start, end = 0, name.find(',')
        name = name[start:end].replace(" ", "_")
        print(link)
        print(name)


        product_type = soup.find('div', class_='catalog-element-card__preview-text').get_text().strip().replace(' ', ' ')
        print("YEAH!")

        print(product_type)


        advantages = soup.find('div', class_='catalog-element__advantages').find('ul').get_text().replace(' ', ' ')
        for i in range(advantages.count('\n')):
            if i % 2 == 1:
                advantages = advantages.replace('\n', '')
        print(advantages)


        product_type = product_type.replace('\n', ' ')




        with open(f"data/{name}.txt", "w", encoding = "utf-8") as file:
            file.write(f"Название товара: {name}\n\nТип: {product_type}\n\nДостоинства: {advantages}\n")


def get_product_links():
    pages = ["https://betaren.ru/catalog/spetsialnye-udobreniya/?PAGEN_1=1",
             "https://betaren.ru/catalog/spetsialnye-udobreniya/?PAGEN_1=2"]
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


if __name__ == '__main__':
    links = get_product_links()
    write_product_info(links)
