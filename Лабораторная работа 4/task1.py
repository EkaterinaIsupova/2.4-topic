class Pet:
    """ Базовый класс Питомец. """

    def __init__(self, name: str, color: str, age: int):
        """
         Создание и подготовка к работе объекта "Питомец"

        :param name: имя питомца
        :param color: окрас питомца
        :param age: возраст питомца

        Примеры:
        >> > pet0 = Pet("Ted", "orange", 2)  # инициализация экземпляра класса
        """
        self.name = name
        self.color = color
        self.age = age

    @property
    def name(self) -> str:
        """Свойства для установки имени. """
        """Возвращает имя питомца."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Устанавливает имя питомца."""
        self._name = new_name

    @property
    def color(self) -> str:
        """Свойства для установки окраса. """
        """Возвращает окрас питомца."""
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        """Устанавливает окрас питомца."""
        self._color = new_color

    @property
    def age(self) -> int:
        """Свойства для установки возраста. """
        """Возвращает возраст питомца.
        Примеры:
        >> > print(pet1.age)
        """
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        """Функция, которая устанавливает возраст питомца.
        Примеры:
        >> > pet0.age = 3
        """
        if not isinstance(new_age, int):
            raise TypeError("Возраст питомца должен быть типа int")
        if new_age <= 0:
            raise ValueError("Возраст питомца должен быть положительным числом")
        self._age = new_age

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'

    def __str__(self) -> str:
        return f"Имя домашнего питомца {self.name}. Его цвет {self.color}. Его возраст: {self.age}"

    def favorite_food(self) -> str:
        """Возвращает любимую еду питомца.
        Примеры:
        :return: Строка, которая показывает, какая любимая у питомца по имени "..."
        >> > print(pet0.favorite_food())
        """
        return f"Питомец {self.name} любит мясо"

    def habitation(self) -> str:
        """Возвращает место проживания питомца. Pet -это домашний питомец,
        значит он живёт в доме с хозяином
        Примеры:
        :return: Строка, которая показывает, какая любимая у питомца по именигде живёт питомец "..."
        >> > print(pet0.habitation())
        """
        return f"Питомец {self.name} живёт в доме хозяина."


class Cat(Pet):
    """ Класс Кот - наследник Питомца. """

    """ Так как кот - это домашний питомец, то он живёт с хозяином в доме, метод наследуется"""
    def habitation(self):
        super().habitation()

    def __str__(self) -> str:
        """ Перегружаю __str__, так как говорю уже конкретно о коте """
        return f"Имя кота {self.name}. Его цвет {self.color}. Его возраст: {self.age}"

    def favorite_food(self) -> str:
        """ Перегружаю favorite_food, так как кот ест ешё и рыбу"""
        """Функция, которая возвращает любимую еду кота.
        Примеры:
        >> > print(cat0.favorite_food())
        """
        return f"Кот {self.name} любит мясо и рыбу"

    def sound(self) -> str:
        """ Перегружаю sound, так как у кота свой звук "мяу" """
        """Функция, которая возвращает звук кота.
        Примеры:
        >> > print(cat0.sound())
        """
        return f"Кот {self.name} говорит: Мяу!"


class Dog(Pet):
    """ Класс Пёс - наследник Питомца. """

    def habitation(self):
        """ Так как пёс - это домашний питомец, то он живёт с хозяином в доме, метод наследуется"""
        super().habitation()

    def __str__(self) -> str:
        """ Перегружаю __str__, так как говорю уже конкретно о псе """
        return f"Имя пса {self.name}. Его цвет {self.color}. Его возраст: {self.age}"

    def favorite_food(self) -> str:
        """ Перегружаю favorite_food, так как пёс любит помимо мяса ещё и кости"""
        """Функция, которая возвращает любимую еду пса.
        Примеры:
        >> > print(dog0.favorite_food())
        """
        return f"Пёс {self.name} любит мясо и кости"

    def sound(self) -> str:
        """ Перегружаю sound, так как у пса свой звук "гав" """
        """Функция, которая возвращает звук пса.
        Примеры:
        >> > print(dog0.sound())
        """
        return f"Пёс {self.name} говорит: Гав!"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
