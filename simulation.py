import time
from actions import Actions
from map import Map
from validators import validate_commands


class Simulation:

    """Класс симуляции мира"""

    def __init__(self, width: int, height: int, show_logs: bool = False) -> None:
        self.world_map = Map(width, height)
        self.show_logs = show_logs
        self.actions = Actions(self.world_map)
        self.actions.init_actions()
        self.count = 0

    def next_turn(self):

        """Симулируется и рендерится один ход"""

        self.actions.turn_actions()
        self.count += 1
        self.render()
        print('Проведенное количество ходов - ', self.count)
        print()
        self.actions.logs = []
        time.sleep(2)

    def render(self):

        """Рендер xодd"""

        self.world_map.show_entities()
        if self.show_logs:
            print(*self.actions.logs, sep='\n')

    def start_simulation(self):

        """Запуск бесконечого цикла симуляции и рендеринга"""

        count_moves = 10
        while True:
            for i in range(count_moves):
                self.next_turn()
            if Simulation.pause_simulation():
                self.count = 0
                print('Симуляция завершена')
                break

    @staticmethod
    def pause_simulation():

        """Приостановка бесконечного цикла симуляции и рендеринга"""

        while True:
            answer = validate_commands(input('Остановить симуляцию? 1 - да, 2 - нет  '))
            if answer == '1':
                return True
            if answer == '2':
                return False
