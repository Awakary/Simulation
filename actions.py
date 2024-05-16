from random import choice

from entity import *
from map import Map


class Actions:

    """Action - действие, совершаемое над миром. Например - сходить всеми существами.
    Это действие итерировало бы существ и вызывало каждому make_move().
    Каждое действие описывается отдельным классом и совершает операции над картой.
     Симуляция содержит 2 массива действий:"""

    def __init__(self, world: Map, show_logs=False):
        self.world = world
        self.entities = [Empty, Grass, Rock, Tree, Herbivore, Predator]
        self.logs = []

    def init_actions(self):

        """действия, совершаемые перед стартом симуляции. Пример - расставить объекты и существ на карте"""

        for entity in self.entities:
            place = choice(list(self.world.map.keys()))
            self.world.map[place] = entity(place[0], place[1])

        for place in self.world.map:
            if self.world.map[place] == ' ':
                self.world.map[place] = choice(self.entities)(place[0], place[1])
        # self.world.map = {place: choice(self.entities)(place[0], place[1])
        #                   for place in self.world.map}

    def turn_actions(self):

        """действия, совершаемые каждый ход.
        Примеры - передвижение существ, добавить травы или травоядных, если их осталось слишком мало"""

        one_circle = []
        for animal in self.world.map.values():
            if isinstance(animal, (Herbivore, Predator)) and animal not in one_circle:
                self.add_entities(self.world)
                animal.make_move(self.world, self.logs)
                one_circle.append(animal)
                self.world.set_cell(animal)
                if isinstance(animal, Predator):
                    animal.attack(self.world, self.logs)
                if animal.hp == 0:
                    animal.lost(self.world, self.logs)

    def add_entities(self, world):
        food = [Grass, Herbivore]
        add_count = 3 if self.world.width >= 5 and self.world.height >= 5 else 1
        for cls in food:
            while len(world.find_entity_cells(cls)) < add_count:
                if not world.find_entity_cells(Empty):
                    place = choice(world.find_entity_cells(Rock)+world.find_entity_cells(Tree))
                else:
                    place = choice(world.find_entity_cells(Empty))
                self.world.set_cell(cls(place[0], place[1]))
                self.logs.append(f'Добавлен(а) {cls.name} на клетку {place}')



