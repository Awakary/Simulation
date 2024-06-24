import time
import threading
from actions import Actions
from map import Map
from render import Render


class Simulation:

    """Класс симуляции мира"""

    def __init__(self, width: int, height: int, show_logs: bool = False) -> None:
        self._world_map = Map(width, height)
        self._show_logs = show_logs
        self._actions = Actions(self._world_map)
        self._actions.init_actions()
        self._count = 0

    def _next_turn(self):

        """Симулируется и рендерится один ход"""

        self._actions.turn_actions()
        self._count += 1
        self._render()
        print('Проведенное количество ходов - ', self._count)
        print()
        self._actions.logs = []
        time.sleep(2)

    def _render(self):

        """Рендер xодd"""

        Render.show_objects(self._world_map)
        if self._show_logs:
            print(*self._actions.logs, sep='\n')

    def start_simulation(self):

        """Запуск бесконечого цикла симуляции и рендеринга"""

        def loop(user_input, time=0.5):
            while not user_input.wait(time):
                self._next_turn()

        user_input = threading.Event()
        threading.Thread(target=loop, args=[user_input], daemon=True).start()
        input('Нажмите Enter для остановки симуляции')
        user_input.set()
