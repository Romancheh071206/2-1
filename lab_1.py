import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def is_empty_book(self) -> bool:
        """
        Функция которая проверяет является ли книга новой (никогда не открывалась)

        :return: Является ли книга новой

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.is_empty_book()
        """
        ...

    def open_book_on_page(self, page_number: int) -> None:
        """
        Открытие книги на определенной странице.

        :param page_number: Номер страницы для открытия
        :raise ValueError: Если номер страницы выходит за пределы книги, то вызываем ошибку

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.open_book_on_page(100)
        """
        if not isinstance(page_number, int):
            raise TypeError("Номер страницы должен быть типа int")
        if page_number < 1 or page_number > self.pages:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.pages}")
        ...

    def add_bookmark(self, page_number: int) -> None:
        """
        Добавление закладки в книгу.

        :param page_number: Номер страницы для закладки
        :raise ValueError: Если номер страницы выходит за пределы книги, то вызываем ошибку

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.add_bookmark(500)
        """
        if not isinstance(page_number, int):
            raise TypeError("Номер страницы должен быть типа int")
        if page_number < 1 or page_number > self.pages:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.pages}")
        ...


class Smartphone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_capacity: Ёмкость аккумулятора в мАч

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть типа str")
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        if not model:
            raise ValueError("Модель не может быть пустой")
        self.model = model

        if not isinstance(battery_capacity, int):
            raise TypeError("Ёмкость аккумулятора должна быть типа int")
        if battery_capacity <= 0:
            raise ValueError("Ёмкость аккумулятора должна быть положительным числом")
        self.battery_capacity = battery_capacity

    def is_phone_on(self) -> bool:
        """
        Функция которая проверяет включен ли смартфон

        :return: Включен ли смартфон

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        >>> phone.is_phone_on()
        """
        ...

    def make_call(self, phone_number: str) -> None:
        """
        Совершение звонка на указанный номер.

        :param phone_number: Номер телефона для звонка
        :raise ValueError: Если номер телефона некорректный, то вызываем ошибку

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        >>> phone.make_call("+79123456789")
        """
        if not isinstance(phone_number, str):
            raise TypeError("Номер телефона должен быть типа str")
        if len(phone_number) < 5:
            raise ValueError("Номер телефона должен содержать минимум 5 символов")
        ...

    def install_application(self, app_name: str) -> None:
        """
        Установка приложения на смартфон.

        :param app_name: Название приложения для установки
        :raise ValueError: Если название приложения пустое, то вызываем ошибку

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        >>> phone.install_application("Telegram")
        """
        if not isinstance(app_name, str):
            raise TypeError("Название приложения должно быть типа str")
        if not app_name:
            raise ValueError("Название приложения не может быть пустым")
        ...


class SocialNetwork:
    def __init__(self, name: str, users_count: int, founded_year: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param users_count: Количество пользователей
        :param founded_year: Год основания

        Примеры:
        >>> network = SocialNetwork("Facebook", 2910000000, 2004)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть типа str")
        if not name:
            raise ValueError("Название социальной сети не может быть пустым")
        self.name = name

        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.users_count = users_count

        if not isinstance(founded_year, int):
            raise TypeError("Год основания должен быть типа int")
        if founded_year <= 0:
            raise ValueError("Год основания должен быть положительным числом")
        self.founded_year = founded_year

    def is_network_active(self) -> bool:
        """
        Функция которая проверяет активна ли социальная сеть (работает ли)

        :return: Активна ли социальная сеть

        Примеры:
        >>> network = SocialNetwork("Facebook", 2910000000, 2004)
        >>> network.is_network_active()
        """
        ...

    def create_user_profile(self, username: str, email: str) -> None:
        """
        Создание профиля пользователя.

        :param username: Имя пользователя
        :param email: Email пользователя
        :raise ValueError: Если имя пользователя или email некорректны, то вызываем ошибку

        Примеры:
        >>> network = SocialNetwork("Facebook", 2910000000, 2004)
        >>> network.create_user_profile("ivan_ivanov", "ivan@example.com")
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if len(username) < 3:
            raise ValueError("Имя пользователя должно содержать минимум 3 символа")

        if not isinstance(email, str):
            raise TypeError("Email должен быть типа str")
        if "@" not in email or "." not in email:
            raise ValueError("Email должен быть корректным")
        ...

    def add_friendship(self, user1_id: int, user2_id: int) -> None:
        """
        Добавление дружбы между двумя пользователями.

        :param user1_id: ID первого пользователя
        :param user2_id: ID второго пользователя
        :raise ValueError: Если пользователи пытаются добавить сами себя в друзья, то вызываем ошибку

        Примеры:
        >>> network = SocialNetwork("Facebook", 2910000000, 2004)
        >>> network.add_friendship(12345, 54321)
        """
        if not isinstance(user1_id, int):
            raise TypeError("ID пользователя должен быть типа int")
        if not isinstance(user2_id, int):
            raise TypeError("ID пользователя должен быть типа int")
        if user1_id == user2_id:
            raise ValueError("Пользователь не может добавить самого себя в друзья")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации