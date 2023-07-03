class Search:
    def __init__(self, mass: list[str]):
        """
        --- ЭТО ИНИТ ---
        !! ОН ВЫПОЛНЯЕТСЯ ПРИ ОБЪЯВЛЕНИИ КЛАССА И НИЧЕГО НЕ ВОЗРАЩАЕТ !!
        Получает массив данных
        *В массивах строки*
        """
        self.value_mass = set(mass)

    def search(self, massage: str) -> set[str]:
        """
        --- ЭТО ПОИСК ВСЕХ ВХОЖДЕНИЙ ПРОДУКТА ---
        Функция ищет все вхождения строку
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
        Функция ищет все вхождения в строку
        Принемает сроку сообщения
        Возвращает по строчно
        !!! ЭТО ГЕНИРАТОР !!!
        """

        for item in massage.split(" "):
            if self.value_mass.__contains__(item):
                yield item
