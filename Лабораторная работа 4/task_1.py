if __name__ == "__main__":
    import doctest
    class RolledProfile:
        """Базовый класс "Прокатный профиль" """
        def __init__(self, size: str, profile: str, steel_grade: str = "С235"):
            """
             Создание и подготовка к работе объекта "Прокатный профиль"

            :param size: Размер профиля
            :param profile: Вид профиля
            :param steel_grade: Марка стали
            атрибуты инкапсулированы для предотвращения присвоения им значений напрямую (без проверок)

            Пример:
            >>> rolledprofile = RolledProfile("50x70", "Прямоугольный", "С245")
            """
            self._size = None
            self._profile = None
            self._steel_grade = "С235"
            self.size = size
            self.profile = profile
            self.steel_grade = steel_grade

        @property
        def size(self) -> str:
            return self._size

        @size.setter
        def size(self, size: str) -> None:
            # проверка по списку размеров
            if not isinstance(size, str):
                raise TypeError("Размер должен быть строкой")
            self._size = size

        @property
        def profile(self) -> str:
            return self._profile

        @profile.setter
        def profile(self, profile: str) -> None:
            # проверка по списку профилей
            if not isinstance(profile, str):
                raise TypeError("Профиль должен быть строкой")
            self._profile = profile

        @property
        def steel_grade(self) -> str:
            return self._steel_grade

        @steel_grade.setter
        def steel_grade(self, steel_grade: str) -> None:
            # проверка по списку марок стали
            if not isinstance(steel_grade, str):
                raise TypeError("Марка стали должна быть строкой")
            self._steel_grade = steel_grade

        def mass(self) -> float:
            """
            Метод возвращает значение массы профиля
            :return: Дробное число в кг

            Пример:
            >>> rolledprofile = RolledProfile("50x70", "Прямоугольный", "С245")
            >>> mass = rolledprofile.mass()
            """
            ...

        def specification(self) -> str:
            """
            Метод возвращает спецификацию на основные характеристики сечения
            :return: str

            Пример:
            >>> rolledprofile = RolledProfile("50x70", "Прямоугольный", "С245")
            >>> specification = rolledprofile.specification()
            """
            return f""" Прокатный профиль {self._size}, {self._profile}:
            Площадь A =
            Осевые моменты инерции:
                Jx =
                Jy =
            Осевые моменты сопротивления:
                Wx =
                Wy =
            Осевые радиусы инерции:
                ix =
                iy =   
            """

        def __str__(self):
            return f'''Прокатный профиль: 
            размер: {self._size};
            сечение: {self._profile};
            марка стали: {self._steel_grade}'''

        def __repr__(self):
            return f'{self.__class__.__name__}({self._size!r}, {self._profile!r}, {self._steel_grade!r})'


    class IBeam(RolledProfile):
        """Дочерний класс "Двутавр", унаследован от класса "Прокатный профиль" """
        def __init__(self, size: str, steel_grade: str = "С235"):
            """
            Создание и подготовка к работе объекта "Прокатный профиль"
            
            :param size: Размер двутавра
            :param steel_grade: Марка стали

            Пример:
            >>> ibeam = IBeam("12Б1", "С245")
            """
            if not isinstance(size, str):
                raise TypeError("Размер должен быть строкой")
            if not isinstance(steel_grade, str):
                raise TypeError("Марка стали должна быть строкой")
            super().__init__(size, "Двутавр", steel_grade)

        def specification(self):
            """
            Метод "спецификация" перегружен для добавления в спецификацию геометрических характеристик двутавра
            :return: str

            Пример:
            >>> ibeam = IBeam("12Б1", "С245")
            >>> specification = ibeam.specification()
            """
            return f"""{super().specification()}
            Геометрические характеристики Двутавра {self._size}:
                Высота двутавра h =
                Ширина полки b =
                Толщина стенки s =
                Толщина полки t =
                Радиус сопряжения r =
            """

