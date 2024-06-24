from abc import ABC
from cell import Cell


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


class Tree(Entity):

    """Класс дерева"""

    name = 'Дерево'

    def show(self):
        return '🌲'


class Creature(Entity):

    """Родительский класс для животных"""

    def __init__(self, x: int, y: int, hungry: int, hp: int) -> None:
        super().__init__(x, y)
        self._hungry = hungry
        self._hp = hp

    def make_move(self, *args):

        """Передвижение животного"""

        pass

    # def _disappeared(self, world, logs):
    #
    #     """Исчезновение животного"""
    #
    #     pass


class Herbivore(Creature):

    """Класс травоядного"""

    name = 'Заяц'
    food = Grass

    def __init__(self, x: int, y: int, hungry: int = 4, hp: int = 3) -> None:
        super().__init__(x, y, hungry, hp)

    def show(self):
        return '🐰'

    def make_move(self, name, food, world, path, logs):
        if self._hp == 0:
            self._disappeared(world, logs)
        else:
            old_cell = Cell(self.x, self.y)
            if self._hungry < 2:
                self.x, self.y = path.bfs(self, food=True)
                self._hungry += 2
                logs.append(f'{name} {old_cell.x, old_cell.y} съел(а) ресурс на клетке {self.x, self.y}')

            else:
                self.x, self.y = path.bfs(self, food=False)
                self._hungry -= 1
                logs.append(f'{name} с клетки {old_cell.x, old_cell.y} перешeл(шла) на клетку {self.x, self.y}')
            world.set_empty(old_cell)
            world.set_object(self)

    def lost_hp(self, logs):

        """Уменьшение здоровья"""

        self._hp -= 1
        logs.append(f'{self.name} на клетке {self.x, self.y} потерял 1 hp от здоровья')

    def _disappeared(self, world, logs):

        """Исчезновение животного"""

        world.set_empty(Cell(self.x, self.y))
        logs.append(f'{self.name} c клетки {self.x, self.y} исчез(hp стал равным 0)')


class Predator(Creature):

    """Класс хищника"""

    name = 'Лиса'
    food = Herbivore

    def __init__(self, x: int, y: int, hungry: int = 5, hp: int = 3) -> None:
        super().__init__(x, y, hungry, hp)
        self._hungry = hungry
        self._hp = hp

    def show(self):
        return '🦊'

    def attack(self, world, logs):

        """Укус травоядного(хищник кусает травоядное на всех соседних клетках)"""

        herbivore_cells = world.find_objects(Herbivore)
        for x, y in herbivore_cells:
            if abs(self.x - x) in [0, 1] and abs(self.y - y) in [0, 1]:
                herbivore = world.map[x, y]
                herbivore.lost_hp(logs)

    def make_move(self, name, food, world, path, logs):
        old_cell = Cell(self.x, self.y)
        if self._hungry < 3:
            self.x, self.y = path.bfs(self, food=True)
            self._hungry += 3
            logs.append(f'{name} {old_cell.x, old_cell.y} съел(а) ресурс на клетке {self.x, self.y}')

        else:
            self.x, self.y = path.bfs(self, food=False)
            self._hungry -= 1
            logs.append(f'{name} с клетки {old_cell.x, old_cell.y} перешeл(шла) на клетку {self.x, self.y}')
        world.set_empty(old_cell)
        world.set_object(self)
        self.attack(world, logs)
