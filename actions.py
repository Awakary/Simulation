from random import choice
from breadth_first_search import Path
from cell import Empty
from entity import *
from map import Map
from render import Render


class Actions:

    """Action - совершаемое действие в мире"""

    def __init__(self, world: Map):
        self.world = world
        self.path = Path(world)
        self._objects = [Empty, Grass, Rock, Tree, Herbivore, Predator]
        self.logs = []

    def init_actions(self):

        """Расставляет существ на карте"""

        for entity in self._objects:
            places = self.world.map
            cell = Cell(*choice(list(filter(lambda x: places[x] == ' ', places))))
            self.world.map[cell.x, cell.y] = entity(cell.x, cell.y)

        for key in self.world.map:
            if self.world.map[key] == ' ':
                cell = Cell(*key)
                self.world.map[cell.x, cell.y] = choice(self._objects)(cell.x, cell.y)

        Render.show_objects(self.world)
        print('Карта мира сформирована', '\n')

    def turn_actions(self):

        """Действия за один ход"""

        one_circle = []
        for animal in self.world.map.values():
            if isinstance(animal, (Herbivore, Predator)) and animal not in one_circle:
                self.add_entities(self.world)
                animal.make_move(animal.name, animal.food, self.world, self.path, self.logs)
                one_circle.append(animal)

    def add_entities(self, world):

        """Добавляет пустые клетки, траву, зайцев"""

        add_list = [Empty, Herbivore, Grass, Empty]
        for cls in add_list:
            if cls == Empty:
                add_count = 2
            elif cls == Herbivore:
                add_count = len(world.find_objects(Predator))
            else:
                add_count = len(world.find_objects(Herbivore))
            while len(world.find_objects(cls)) < add_count:
                if cls == Empty or not world.find_objects(Empty):
                    cell = Cell(*choice(list(world.map.keys())))
                else:
                    cell = Cell(*choice(world.find_objects(Empty)))
                self.world.set_object(cls(cell.x, cell.y))
                self.logs.append(f'Добавлен(а) {cls.name} на клетку {cell.x, cell.y}')
