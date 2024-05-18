from random import choice
from entity import *
from map import Map


class Actions:

    """Action - соыершаемое действие в мире"""

    def __init__(self, world: Map):
        self.world = world
        self.entities = [Empty, Grass, Rock, Tree, Herbivore, Predator]
        self.logs = []

    def init_actions(self):

        """Расставляет существ на карте"""

        for entity in self.entities:
            places = self.world.map
            place = choice(list(filter(lambda x: places[x] == ' ', places)))
            self.world.map[place] = entity(place[0], place[1])

        for place in self.world.map:
            if self.world.map[place] == ' ':
                self.world.map[place] = choice(self.entities)(place[0], place[1])

        self.world.show_entities()
        print('Карта мира сформирована', '\n')

    def turn_actions(self):

        """Действия за один ход"""

        one_circle = []
        for animal in self.world.map.values():
            if isinstance(animal, (Herbivore, Predator)) and animal not in one_circle:
                if animal.hp == 0:
                    animal.disappeared(self.world, self.logs)
                else:
                    self.add_entities(self.world)
                    animal.make_move(animal.name, animal.food, self.world, self.logs)
                    one_circle.append(animal)
                    self.world.set_cell(animal)
                    if isinstance(animal, Predator):
                        animal.attack(self.world, self.logs)

    def add_entities(self, world):

        """Добавляет пустые клетки, траву, зайцев"""

        add_list = [Empty, Herbivore, Grass, Empty]
        for cls in add_list:
            if cls == Empty:
                add_count = 2
            elif cls == Herbivore:
                add_count = len(world.find_entity_cells(Predator))
            else:
                add_count = len(world.find_entity_cells(Herbivore))
            while len(world.find_entity_cells(cls)) < add_count:
                if cls == Empty or not world.find_entity_cells(Empty):
                    place = choice(list(world.map.keys()))
                else:
                    place = choice(world.find_entity_cells(Empty))
                self.world.set_cell(cls(place[0], place[1]))
                self.logs.append(f'Добавлен(а) {cls.name} на клетку {place}')
