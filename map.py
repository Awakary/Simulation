from entity import *


class Map:

    """Карта, содержит в себе коллекцию для хранения существ и их расположения. Советую не спешить использовать
    двумерный массив или список списков, а подумать какие ещё коллекции могут подойти"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.map = {(i, j): ' ' for i in range(height) for j in range(width)}

    def set_cell(self, entity):
        self.map[entity.x, entity.y] = entity

    def clear_cell(self, old_place):
        self.map[old_place[0], old_place[1]] = Empty()

    def find_entity_cells(self, cls):
        return [position for position, entity in self.map.items()
                if type(entity) == cls]


    def show_entities(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.map[i, j].show() + "\t", end='')
            print(i)






