from cell import Empty
from entity import *


class Map:

    """Карта, содержит в себе коллекцию для хранения существ и их расположения"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.map = {(i, j): ' ' for i in range(1, height + 1) for j in range(1, width + 1)}

    def set_object(self, object):

        """Устанавливает сущность на карту"""

        self.map[object.x, object.y] = object

    def set_empty(self, old_cell: Cell):

        """Устанавливает пустую клетку на карте"""

        self.map[old_cell.x, old_cell.y] = Empty()

    def find_objects(self, cls):

        """Ищет указанный вид объектов на карте"""

        return [position for position, object in self.map.items()
                if isinstance(object, cls)]

    def get_cls(self, x, y):

        """Ищет указанный вид объектов на карте"""

        return type(self.map[x, y])
