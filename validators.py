def validate_size(size: str) -> str:

    """функция проверки введенного размера"""

    while True:
        if len(size) == 1 and size in '3456789' or size == '10':
            return size
        else:
            size = input('Введите пожалуйста число от 3 до 10 ')


def validate_commands(number: str) -> str:

    """функция проверки введенного ответа от пользователя"""

    while True:
        if number in '12':
            return number
        else:
            number = input('Ввведите пожауйста цифру: 1 - да, 2 - нет ')


