from headers import *
from random import *
from objects import *

class Brick(Object):
    # Class for bricks 
    def __init__(self, x, y):
        strength_list = [1, 2, 3]
        self.__value = [random.choice(strength_list)]
        self.__gone = 0
        self.__body = [['_', '_', '_', '_', self.__value[0], '_', '_', '_', '_']]
        Object.__init__(self, x, y)

    def reset(self, grid, x, y):
        strength_list = [1, 2, 3]
        self.__value = [random.choice(strength_list)]
        self.__gone = 0
        self.__body = [['_', '_', '_', '_', self.__value[0], '_', '_', '_', '_']]

    def get_value(self):
        val = self.__value[0]
        return val
    
    def set_value(self, val):
        self.__value[0] = val

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
            val = self.get_value()
            if val == 1:
                if i == x + 4:
                    grid[y][i] = str(Fore.BLACK + Back.WHITE + Style.BRIGHT + str(self.get_value()) + Style.RESET_ALL)
                else:
                    grid[y][i] = str(Fore.BLACK + Back.WHITE + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)
            elif val == 2:
                if i == x + 4:
                    grid[y][i] = str(Fore.BLACK + Back.BLUE + Style.BRIGHT + str(self.get_value()) + Style.RESET_ALL)
                else:
                    grid[y][i] = str(Fore.BLACK + Back.BLUE + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)
            elif val == 3:
                if i == x + 4:
                    grid[y][i] = str(Fore.BLACK + Back.GREEN + Style.BRIGHT + str(self.get_value()) + Style.RESET_ALL)
                else:
                    grid[y][i] = str(Fore.BLACK + Back.GREEN + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)
            elif val == 'X':
                if i == x + 4:
                    grid[y][i] = str(Fore.BLACK + Back.RED + Style.BRIGHT + str(self.get_value()) + Style.RESET_ALL)
                else:
                    grid[y][i] = str(Fore.BLACK + Back.RED + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)
            elif val == '*' and self.get_gone() == 0:
                if i == x + 4:
                    grid[y][i] = str(Fore.WHITE + Back.YELLOW + Style.BRIGHT + str(self.get_value()) + Style.RESET_ALL)
                else:
                    grid[y][i] = str(Fore.BLACK + Back.YELLOW + Style.BRIGHT + str(self.__body[0][i - x]) + Style.RESET_ALL)

