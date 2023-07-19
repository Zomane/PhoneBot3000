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

        try:
            product_type = soup.find('div', class_='catalog-element-card__structure').get_text().strip()
        except:
            try:
                product_type = soup.find('span', class_='active-i-text').get_text().strip()
            except:
                try:
                    if type(product_type) == 'NoneType':
                        product_type = soup.find('catalog-element-card__preview-text').find_next('p').get_text().strip()
                except:
                    if type(product_type) == 'NoneType':
                        product_type = soup.find('catalog-element-card__preview-text').find('p').get_text().strip()
        finally:
            pass

        print(product_type)
        try:
            compound = soup.find('p', class_='active-ingredients').get_text()
        except:
            try:
                compound = soup.find('span', class_='active-i-text').find_next('p').get_text()
            except:
                compound = termcolor.colored("Состав не найден", "red")
        print(compound)

        advantages = soup.find('div', class_='catalog-element__advantages').find('ul').get_text().replace(' ', ' ')
        for i in range(advantages.count('\n')):
            if i % 2 == 1:
                advantages = advantages.replace('\n', '')
        print(advantages)

        try:
            product_effect = soup.find(string='Механизм действия ').parent.parent.text.replace(' ', ' ')
        except:
            try:
                product_effect = soup.find(string='Механизм действия').parent.parent.text.replace(' ', ' ')
            except:
                try:
                    product_effect = soup.find(string="Пирипроксифен – синтетический аналог ювенильного гормона, механизм действия которого связан с необратимыми нарушениями гормонального баланса в организме вредителей.").parent.text.replace(' ', ' ')
                except:
                    try:
                        product_effect = soup.find(string="Ацетамиприд о").parent.text.replace(' ', ' ')
                    except:
                        try:
                            product_effect = soup.find(string=re.compile("Высокоэффективен против резистентных рас насекомых.")).parent.text.replace(' ', ' ')
                        except:
                            product_effect = termcolor.colored("ИНФА НЕ НАЙДЕНА!", "red")
        product_effect = product_effect.replace('\n', '')
        print(product_effect)

        try:
            about_product = soup.find(string="Класс опасности ").parent.parent.parent.parent.text.replace(' ', ' ')
        except:
            try:
                about_product = soup.find(string="Класс опасности").parent.parent.parent.parent.text.replace(' ', ' ')
            except:
                about_product = termcolor.colored("Общая инфа не найдена!", "red")

        about_product = about_product.replace('\n', ' ')
        print(about_product)


        with open(f"data/{name}.txt", "w", encoding = "utf-8") as file:
            file.write(f"Название товара: {name}\n\nТип: {product_type}\n\nСостав: {compound}\n\nДостоинства: {advantages}\n\n{product_effect}\n\n{about_product}\n")


def get_product_links():
    pages = ["https://betaren.ru/catalog/sredstva-zashchity-rasteniy/?PAGEN_1=1",
             "https://betaren.ru/catalog/sredstva-zashchity-rasteniy/?PAGEN_1=2",
             "https://betaren.ru/catalog/sredstva-zashchity-rasteniy/?PAGEN_1=3",
             "https://betaren.ru/catalog/sredstva-zashchity-rasteniy/?PAGEN_1=4",
             "https://betaren.ru/catalog/sredstva-zashchity-rasteniy/?PAGEN_1=5",
             "https://betaren.ru/catalog/sredstva-zashchity-rasteniy/?PAGEN_1=6"]
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
