class Cell:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Empty(Cell):

    """ Класс пустой клетки"""

    name = 'Пустая клетка'

    def show(self):
        return '⬛'
