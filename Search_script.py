class Search:
    def __init__(self, mass: list[str]):
        """
        --- ЭТО ИНИТ ---
        !! ОН ВЫПОЛНЯЕТСЯ ПРИ ОБЪЯВЛЕНИИ КЛАССА И НИЧЕГО НЕ ВОЗРАЩАЕТ !!
        Получает массив с продуктами и массив с растениями
        *В массивах строки*
        """
        self.value_mass = set(mass)

    def search(self, massage: str) -> set[str]:
        """
        --- ЭТО ПОИСК ВСЕХ ВХОЖДЕНИЙ ПРОДУКТА ---
        Функция ищет все вхождения продуктов строку
        Принемает сроку сообщения
        Возвращает set с массивом, в массиве строки
        """
        context_product = []
        for item in massage.split(" "):
            if self.value_mass.__contains__(item):
                context_product.append(item)
        return set(context_product)

    def search_gen(self, massage: str) -> set[str]:
        """
        --- ЭТО ПОИСК ПРОДУКТА (ГЕНЕРАТОР) ---
        Функция ищет все вхождения продуктов в строку
        Принемает сроку сообщения
        Возвращает по строчно
        !!! ЭТО ГЕНИРАТОР !!!
        """

        for item in massage.split(" "):
            if self.value_mass.__contains__(item):
                yield item


if __name__ == "__main__":
    """ это нужно для теста класса """

    mass1 = ['geg', 'kek', 'lol', 'lolchik', 'hohli', 'ghidi', 'pops', 'opps', 'lols', 'fals', 'jji']
    mass2 = ['fafh', 'kakh', 'paph', 'acab', 'nazi', 'nasvai', 'kkk', 'lll', 'errrno', 'lokj']
    msgs = ['Покажи им кто тут жид', 'geg in doma', 'keks ne doma', 'falk ne pon', 'acab reallino',
            'ac hihih ne nu a cho ia kek and lol',
            'ac hihih ne nu a cho and lol', 'ac hihih ne nu a cho and lol', ' ac hihih ne nu a cho and lol']
    test_class = Search(mass1)
    test_class2 = Search(mass2)

    print('Тест функции search')
    for i in msgs:
        try:
            print(next(test_class.search_gen(i)))
        except:
            print('Конец генератора')

    print('Тест функции search')
    for i in msgs:
        print(str(test_class.search(i)))

    print('Тест функции search_gen')
    for i in msgs:
        try:
            print(next(test_class2.search_gen(i)))
        except:
            print('Конец генератора')

    print('Тест функции search')
    for i in msgs:
        print(test_class2.search(i))
