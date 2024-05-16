import random
from abc import ABC


class Entity(ABC):

    """#Корневой абстрактный класс для всех существ и объектов существующих в симуляции"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        pass


class Grass(Entity):

    name = 'Трава'

    """ресурс для травоядных"""

    def show(self):
        return '🌸'


class Rock(Entity):

    """статичный объект"""

    name = 'Гора'

    def show(self):
        return '🗻'


class Empty(Entity):

    """пустой объект"""

    name = 'Пустая клетка'

    def show(self):
        return '⬛'


class Tree(Entity):

    """статичный объект"""

    name = 'Дерево'

    def show(self):
        return '🌲'


class Creature(Entity):

    """Абстрактный класс, наследуется от Entity. Существо, имеет скорость (сколько клеток может пройти за 1 ход),
     количество HP. Имеет абстрактный метод make_move() - сделать ход.
      Наследники будут реализовывать этот метод каждый по-своему"""

    def __init__(self, x: int, y: int, hungry: int, hp: int) -> None:
        super().__init__(x, y)
        self.hungry = hungry
        self.hp = hp

    def make_move(self, *args, **kwargs):
        pass

    def lost(self, world, logs):
        world.clear_cell((self.x, self.y))
        logs.append(f'{self} исчез')


class Herbivore(Creature):
    """Травоядное, наследуется от Creature.
    Стремятся найти ресурс (траву), может потратить свой ход
    на движение в сторону травы, либо на её поглощение."""

    name = 'Заяц'

    def __init__(self, x: int, y: int, hungry: int = 5, hp: int = 3) -> None:
        super().__init__(x, y, hungry, hp)

    def make_move(self, world, logs):
        old_place = self.x, self.y
        if self.hungry < 3:
            self.x, self.y = random.choice(world.find_entity_cells(Grass))
            self.hungry += 3
            logs.append(f'Заяц с клетки {old_place} съел траву на клетке {self.x, self.y}')

        else:
            self.x, self.y = random.choice(world.find_entity_cells(Empty))
            self.hungry -= 1
            logs.append(f'Заяц с клетки {old_place} перешел на клетку {self.x, self.y}')
        world.clear_cell(old_place)

    def show(self):
        return '🐰'


class Predator(Creature):

    """Хищник, наследуется от Creature. В дополнение к полям класса Creature, имеет силу атаки.
    На что может потратить ход хищник:
    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного
    уменьшается на силу атаки хищника. Если значение HP жертвы опускается до 0, травоядное исчезает"""

    name = 'Лиса'

    def __init__(self, x: int, y: int, hungry: int = 5, hp: int = 3) -> None:
        super().__init__(x, y, hungry, hp)
        self.hungry = hungry
        self.hp = hp

    def make_move(self, world, logs):
        old_place = self.x, self.y
        if self.hungry < 4:
            self.x, self.y = random.choice((world.find_entity_cells(Herbivore)))
            self.hungry += 4
            logs.append(f'Лиса с клетки {old_place} съела зайца на клетке {self.x, self.y}')

        else:
            self.x, self.y = random.choice((world.find_entity_cells(Empty)))
            self.hungry -= 1
            logs.append(f'Лиса с клетки {old_place} перешла на клетку {self.x, self.y}')
        world.clear_cell(old_place)


    def show(self):
        return '🦊'

    def attack(self, world, logs):
        herbivore_cells = world.find_entity_cells(Herbivore)
        for x, y in herbivore_cells:
            if abs(self.x - x) <= 1 and abs(self.y - y) <= 1:
                world.map[x, y].hp -= 1
                logs.append(f'Уменьшилось здоровье зайца на клетке {x, y}')
