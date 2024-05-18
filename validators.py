def validate_size(size: str) -> str:

    """Проверяет введенный размер"""

    while True:
        if len(size) == 1 and size in '456789' or size == '10':
            return size
        else:
            size = input('Введите пожалуйста число от 4 до 10 ')


def validate_commands(number: str) -> str:

    """Проверяет введенную команду от пользователя"""

    while True:
        if number == '1' or number == '2':
            return number
        else:
            number = input('Ввведите пожауйста цифру: 1 - да, 2 - нет ')
