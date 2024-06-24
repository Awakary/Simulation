from collections import deque
from cell import Empty


class Path:

    """Класс поиска пути для животного"""

    def __init__(self, world):
        self.world = world
        self.__graph = {}
        for x, y in world.map:
            self.__graph[x, y] = [(v, b) for v, b in self.world.map
                                  if abs(x-v) in (0, 1) and abs(y-b) in (0, 1)
                                  if 0 <= v <= world.height and 0 <= b <= world.width
                                  if (x, y) != (v, b)]

    def is_target_cell(self, entity, neighbour, food=False):

        """Проверка ячейки на соответствие цели животного"""

        if food:
            return isinstance(self.world.map[neighbour], entity.food)
        return isinstance(self.world.map[neighbour], Empty)

    def bfs(self, entity, food=False):

        """Возврашает координаты целевой ячейки на карте"""

        start_cell = (entity.x, entity.y)
        visited, queue = [], deque()
        queue.extend(self.__graph[start_cell])
        while queue:
            active_cell = queue.popleft()
            if active_cell not in visited:
                if self.is_target_cell(entity, active_cell, food=food):
                    return active_cell
                else:
                    queue.extend(self.__graph[active_cell])
                    visited.append(active_cell)
