from headers import *
from random import *
from objects import *

class Brick(Object):
    # Class for bricks 
    def __init__(self, x, y):
        strength_list = [1, 2, 3, 'X']
        self.__value = random.choice(strength_list)
        self.__gone = 0
        self.__body = [['_', '_', '_', '_', '_', '_', '_', '_', '_']]
        Object.__init__(self, x, y)

    def get_value(self):
        val = self.__value
        return val
    
    def set_value(self, val):
        self.__value = val

    def get_gone(self):
        val = self.__gone
        return val

    def set_gone(self, val):
        self.__gone = val

    def dec_value(self):
        self.set_value(self.get_value() - 1)

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
            elif self.__value == 'X':
                grid[y][i] = str(Fore.BLACK + Back.RED + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)
