from headers import *
from random import *
from objects import *

class Brick(Object):
    # Class for bricks 
    def __init__(self, x, y):
        strength_list = [1, 2, 3, 100]
        self.__value = random.choice(strength_list)
        self.__body = [['_', '_', '_', '_', self.__value, '_', '_', '_', '_']]
        Object.__init__(self, x, y)

    def get_value(self):
        return self.__value

    def dec_value(self):
        self.__value = self.__value - 1

    def clear(self, grid, x, y):
        for i in range(x, x + 9):
            grid[y][i] = ' '
    
    def show(self, grid, y, x):
        self.setx(x)
        self.sety(y)
        for i in range(x, x + 9):
            if self.__value == 1:
                grid[y][i] = str(Fore.BLACK + Back.YELLOW + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)
            elif self.__value == 2:
                grid[y][i] = str(Fore.BLACK + Back.BLUE + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)
            elif self.__value == 3:
                grid[y][i] = str(Fore.BLACK + Back.GREEN + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)
            else:
                grid[y][i] = str(Fore.BLACK + Back.RED + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)

    def check_over(self):
        if self.__value <= 0:
            return 1
        else:
            return 0