Simulation 

Симуляция 2D мира, населённого травоядными и хищниками. Кроме животных, мир содержит ресурсы еды, которыми питаются травоядные(зайцы), а также есть статичные объекты(горы, деревья).

В момент запуска игры создается поле симуляции NхМ с существами (наследники класса Entity). В классах описаны  передвижения по карте и действия травоядных и хищников. Ресурсы для еды добавляются, если исчерпаны. Каждый ход состояние карты выводится на экран.

Приложение написано на Python с использованием ООП. В поиске пути реализован алгоритм поиска в ширину. 
