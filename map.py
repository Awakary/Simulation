from entity import *


class Map:

    """Карта, содержит в себе коллекцию для хранения существ и их расположения"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.map = {(i, j): ' ' for i in range(1, height + 1) for j in range(1, width + 1)}

    def set_cell(self, entity):

        """Устанавливает сущность на карту"""

        self.map[entity.x, entity.y] = entity

    def clear_cell(self, old_place):

        """Очищает клетку на карте"""

        self.map[old_place[0], old_place[1]] = Empty()

    def find_entity_cells(self, cls):

        """Ищет клетки, занятые указанным видом сущностей"""

        return [position for position, entity in self.map.items()
                if isinstance(entity, cls)]

    def show_entities(self):

        """Выводит карту на экран"""

        [print(str(i).center(3), end=' ') for i in range(1, self.width + 1)]
        print()
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                print(self.map[i, j].show() + "\t", end='')
            print(i)
