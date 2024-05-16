import time

from actions import Actions
from map import Map
from validators import validate_commands


class Simulation:

    """включает в себя:
    Карту
    Счётчик ходов
    Рендерер поля
    Actions - список действий, исполняемых перед стартом симуляции или на каждом ходу (детали ниже)"""

    def __init__(self, width, height, show_logs=False):
        self.world_map = Map(width, height)
        self.show_logs = show_logs
        self.actions = Actions(self.world_map, self.show_logs)
        self.actions.init_actions()
        self.count = 0

    def next_turn(self):

        """просимулировать и отрендерить один ход"""

        self.actions.turn_actions()
        self.count += 1
        self.render()
        print('Проведенное количество ходов - ', self.count)
        self.actions.logs = []

        time.sleep(2)

    def render(self):

        """рендер xодd"""

        self.world_map.show_entities()
        if self.show_logs:
            print(*self.actions.logs, sep='\n')

    def start_simulation(self):

        """запустить бесконечный цикл симуляции и рендеринга"""

        while True:
            for i in range(10):
                self.next_turn()
            if Simulation.pause_simulation():
                self.count = 0
                print('Симуляция завершена')
                break

    @staticmethod
    def pause_simulation():

        """приостановить бесконечный цикл симуляции и рендеринга"""

        while True:
            answer = validate_commands(input('Остановить симуляцию? 1 - да, 2 - нет  '))
            if answer == '1':
                return True
            if answer == '2':
                return False


