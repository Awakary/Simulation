from map import Map


class Render:

    @staticmethod
    def show_objects(world: Map):

        """Выводит карту на экран"""
        print()
        [print(' '.ljust(2) + str(i).center(3)+"\t", end='') for i in range(1, world.width + 1)]
        print()
        for i in range(1, world.height+1):
            for j in range(1, world.width+1):
                if j == 1:
                    print(str(i).ljust(2), world.map[i, j].show() + "\t", end='', sep='')
                else:
                    print(' '.ljust(2), world.map[i, j].show() + "\t", end='', sep='')
            print()
