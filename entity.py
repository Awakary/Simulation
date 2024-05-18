import random
from abc import ABC


class Entity(ABC):

    """Корневой абстрактный класс для всех существ и объектов существующих в симуляции"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):

        """Выводит изображение класса на экран"""

        pass


class Grass(Entity):

    """Класс ресурса для травоядных"""

    name = 'Трава'

    def show(self):
        return '🌸'


class Rock(Entity):

    """Класс горы"""

    name = 'Гора'

    def show(self):
        return '🗻'


class Empty(Entity):

    """ Класс пустой клетки"""

    name = 'Пустая клетка'

    def show(self):
        return '⬛'


class Tree(Entity):

    """Класс дерева"""

    name = 'Дерево'

    def show(self):
        return '🌲'


class Creature(Entity):

    """Абстрактный класс для животных"""

    def __init__(self, x: int, y: int, hungry: int, hp: int) -> None:
        super().__init__(x, y)
        self.hungry = hungry
        self.hp = hp

    def make_move(self, *args, **kwargs):

        """Передвижение животного"""

        pass

    def disappeared(self, world, logs):

        """Исчезновение животного"""

        pass


class Herbivore(Creature):

    """Класс травоядного"""

    name = 'Заяц'

    def __init__(self, x: int, y: int, hungry: int = 5, hp: int = 3) -> None:
        super().__init__(x, y, hungry, hp)

    def make_move(self, world, logs):
        old_place = self.x, self.y
        if self.hungry < 3:
            self.x, self.y = random.choice(world.find_entity_cells(Grass))
            self.hungry += 3
            logs.append(f'{self.name} с клетки {old_place} съел траву на клетке {self.x, self.y}')

        else:
            self.x, self.y = random.choice(world.find_entity_cells(Empty))
            self.hungry -= 1
            logs.append(f'{self.name} с клетки {old_place} перешел на клетку {self.x, self.y}')
        world.clear_cell(old_place)

    def show(self):
        return '🐰'

    def disappeared(self, world, logs):

        world.clear_cell((self.x, self.y))
        logs.append(f'{self.name} c клетки {self.x, self.y} исчез(hp стал равным 0)')


class Predator(Creature):

    """Класс хищника"""

    name = 'Лиса'

    def __init__(self, x: int, y: int, hungry: int = 5, hp: int = 3) -> None:
        super().__init__(x, y, hungry, hp)
        self.hungry = hungry
        self.hp = hp

    def make_move(self, world, logs):
        old_place = self.x, self.y
        if self.hungry < 3:
            self.x, self.y = random.choice((world.find_entity_cells(Herbivore)))
            self.hungry += 3
            logs.append(f'{self.name} {old_place} съела зайца на клетке {self.x, self.y}')

        else:
            self.x, self.y = random.choice((world.find_entity_cells(Empty)))
            self.hungry -= 1
            logs.append(f'{self.name} с клетки {old_place} перешла на клетку {self.x, self.y}')
        world.clear_cell(old_place)

    def show(self):
        return '🦊'

    def attack(self, world, logs):

        """Укус травоядного(хищник кусает травоядное на всех соседних клетках)"""

        herbivore_cells = world.find_entity_cells(Herbivore)
        for x, y in herbivore_cells:
            if abs(self.x - x) <= 1 and abs(self.y - y) <= 1:
                world.map[x, y].hp -= 1
                logs.append(f'{world.map[x, y].name} на клетке {x, y} потерял 1 hp от здоровья')
