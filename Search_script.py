from tensorflow.core.function.trace_type import Serializable


class Search:
    def __init__(self, product: list[str], plants: list[str]):
        """
        --- ЭТО ИНИТ ---
        !! ОН ВЫПОЛНЯЕТСЯ ПРИ ОБЪЯВЛЕНИИ КЛАССА И НИЧЕГО НЕ ВОЗРАЩАЕТ !!
        Получает массив с продуктами и массив с растениями
        *В массивах строки*
        """
        self.product = set(product)
        self.plants = set(plants)

    def search_new(self, massage: str) -> list[set[str]]:
        """
        --- ЭТО ПОИСК ВСЕХ ВХОЖДЕНИЙ ВСЕГО ---
        Функция ищет все вхождения в строку как продуктов так и растений
        Принемает сроку сообщения
        Возвращает массив с сетами, в сетах строки
        """

        context_product, context_plant = [], []
        for _, item in enumerate(massage.split(" ")):
            if self.product.__contains__(item):
                context_product.append(item)
            elif self.plants.__contains__(item):
                context_plant.append(item)
        return [set(context_product), set(context_plant)]

    def search_product_many(self, massage: str) -> set[str]:
        """
        --- ЭТО ПОИСК ВСЕХ ВХОЖДЕНИЙ ПРОДУКТА ---
        Функция ищет все вхождения продуктов строку
        Принемает сроку сообщения
        Возвращает set с массивом, в массиве строки
        """
        context_product = []
        for _, item in enumerate(massage.split(" ")):
            if self.product.__contains__(item):
                context_product.append(item)
        return set(context_product)

    def search_product_gen(self, massage: str) -> set[str]:
        """
        --- ЭТО ПОИСК ПРОДУКТА (ГЕНЕРАТОР) ---
        Функция ищет все вхождения продуктов в строку
        Принемает сроку сообщения
        Возвращает по строчно
        !!! ЭТО ГЕНИРАТОР !!!
        """

        for _, item in enumerate(massage.split(" ")):
            if self.product.__contains__(item):
                yield item

    def search_plant_many(self, massage: str) -> list[set[str]]:
        """
        --- ЭТО ПОИСК ВСЕХ ВХОЖДЕНИЙ РАСТЕНИЙ ---
        Функция ищет все вхождения растений строку
        Принемает сроку сообщения
        Возвращает set с массивом, в массиве строки
        """

        context_plant = []
        for _, item in enumerate(massage.split(" ")):
            if self.product.__contains__(item):
                context_plant.append(item)
        return set(context_plant)

    def search_plant_gen(self, massage: str) -> set[str]:
        """
        --- ЭТО ПОИСК РАСТЕНИЙ (ГЕНЕРАТОР) ---
        Функция ищет все вхождения астений в строку
        Принемает сроку сообщения
        Возвращает по строчно
        !!! ЭТО ГЕНИРАТОР !!!
        """

        for _, item in enumerate(massage.split(" ")):
            if self.product.__contains__(item):
                yield item


if __name__ == "__main__":
    """ это нужно для теста класса """

    mass1 = ['geg', 'kek', 'lol', 'lolchik', 'hohli', 'ghidi']
    mass2 = ['fafh', 'kakh', 'paph', 'acab', 'nazi', 'nasvai']
    msgs = ['Покажи им кто тут жид', 'geg in doma', 'keks ne doma', 'falk ne pon', 'acab reallino', 'ac hihih ne nu a cho ia kek and lol']
    test_class = Search(mass1, mass2)

    print('Тест функции search_new')
    for i in msgs:
        print(test_class.search_new(i))

    print('Тест функции search_plant_gen')
    for i in msgs:
        try:
            print(next(test_class.search_plant_gen(i)))
        except:
            print('Конец генератора')

    print('Тест функции search_plant_many')
    for i in msgs:
        print(str(test_class.search_plant_many(i)))

    print('Тест функции search_product_gen')
    try:
        print(next(test_class.search_product_gen(i)))
    except:
        print('Конец генератора')

    print('Тест функции search_product_many')
    for i in msgs:
        print(test_class.search_product_many(i))





