from simulation import Simulation
from validators import validate_size, validate_commands

if __name__ == '__main__':
    print('Добро пожаловать в Simulation!')
    while True:
        map_height = validate_size(input('Введите пожалуйста нужную высоту поля (число от 3 до 10) '))
        map_width = validate_size(input('Введите пожалуйста нужную ширину поля (число от 3 до 10) '))
        show_logs = validate_commands(input('Показывать логи действий для объектов да - 1, нет - 2 '))
        game = Simulation(width=int(map_width), height=int(map_height),show_logs=show_logs)
        print('Запуск симуляции')
        game.start_simulation()
        restart = validate_commands(input('Запустить новую симуляцию? 1 - да, 2 - нет '))
        if restart == '2':
            print('Симуляция закрыта')
            break

