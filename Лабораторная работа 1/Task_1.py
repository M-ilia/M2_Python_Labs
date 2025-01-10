
# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Door:
    def __init__(self, width: float, height: float):
        """
         Создание и подготовка к работе объекта "Дверь"

        :param width: Ширина двери
        :param height: Высота двери

        Пример:
        >>> door = Door(1, 2.1)
        """
        if not isinstance(width, (float, int)):
            raise TypeError("Ширина должна быть представлена типом int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        if not isinstance(height, (float, int)):
            raise TypeError("Высота должна быть представлена типом int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")

        self.width = width
        self.height = height
        self.material = None
        self.type_door = None

    def set_material(self, material: str) -> None:
        """
        Назначение материала двери
        :param material: Название материала
        :return: None

        Пример:
        >>> door = Door(1, 2.1)
        >>> door.set_material("Дерево")
        """
        if not isinstance(material, str):
            raise TypeError('Название материала должно быть строкой')
        ...

    def set_type_door(self, type_door: str) -> None:
        """
        Назначение типа двери
        :param type_door: Название типа двери
        :return: None

        Пример:
        >>> door = Door(1, 2.1)
        >>> door.set_type_door("Двупольная распашная")
        """
        if not isinstance(type_door, str):
            raise TypeError('Тип двери должен быть строкой')
        ...


class Wall:
    def __init__(self, length: float, height: float, width: float):
        """
        Создание и подготовка к работе объекта "Стена"
        :param length: Длина стены
        :param height: Высота стены
        :param width: Толщина стены

        Пример:
        >>> wall = Wall(10.5, 3.2, 0.6)
        """
        if not isinstance(length, (float, int)) or not isinstance(height, (float, int)) or not isinstance(width, (float, int)):
            raise TypeError("Вводимые значения должны быть представлены типами int или float")
        elif length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Вводимые числа должны быть положительными")
        else:
            self.length = length
            self.width = width
            self.height = height

    def set_material(self, material: str) -> None:
        """
        Назначение материала стены
        :param material: Название материала стены
        :return: None

        Пример:
        >>> wall = Wall(10.5, 3.2, 0.6)
        >>> wall.set_material("Кирпич")
        """
        if not isinstance(material, str):
            raise TypeError('Название материала должно быть строкой')
        ...

    def add_door(self, door: Door) -> None:
        """
        Добавление двери в стену
        :param door: Экземпляр класса Door
        :return: None

        Пример:
        >>> door = Door(1, 2.1)
        >>> wall = Wall(10.5, 3.2, 0.6)
        >>> wall.add_door(door)
        """
        if not isinstance(door, Door):
            raise TypeError("Необходимо передать экземпляр класса Door")

    def remove_door(self, door: Door) -> None:
        """
        Удаление двери из стены
        :param door: Экземпляр класса Door
        :raise ValueError: Если переданного значения нет в списке элементов стены
        :return: None

        Пример:
        >>> door = Door(1, 2.1)
        >>> wall = Wall(10.5, 3.2, 0.6)
        >>> wall.add_door(door)
        >>> wall.remove_door(door)
        """
        if not isinstance(door, Door):
            raise TypeError("Необходимо передать экземпляр класса Door")
        ...


class House:
    def __init__(self, area: float, floors: int):
        """
        Создание и подготовка к работе объекта "Дом"
        :param area: Площадь здания
        :param floors: Количество этажей

        Пример:
        >>> house = House(125.5, 1)
        """
        self.area = None
        self.floors = None
        self.set_area(area)
        self.set_floors(floors)

    def set_area(self, area: float) -> None:
        """
        Назначение площади здания
        :param area: Площадь здания
        :return: None

        Пример:
        >>> house = House(125.5, 1)
        >>> house.set_area(50.7)
        """
        if not isinstance(area, float):
            raise TypeError("Площадь должна быть представлена типом float")
        if area <= 0.0:
            raise ValueError("Площадь должна быть положительной")

    def set_floors(self, floors: int) -> None:
        """
        Назначение количества этажей
        :param floors: Количество этажей
        :return: None

        Пример:
        >>> house = House(125.5, 1)
        >>> house.set_floors(3)
        """
        if not isinstance(floors, int):
            raise TypeError("Количество этажей должно быть представлено типом int")
        if floors < 1:
            raise ValueError("Количество этажей не может быть меньше 1")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
