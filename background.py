from headers import *

class Background:
    # Constructor function
    def __init__(self):
        self.__ceil = Fore.WHITE + Back.BLACK + Style.BRIGHT + "_" + Style.RESET_ALL
        self.__left_wall = Fore.WHITE + Back.BLACK + Style.BRIGHT + "|" + Style.RESET_ALL
        self.__right_wall = Fore.WHITE + Back.BLACK + Style.BRIGHT + "|" + Style.RESET_ALL

    # Function to create the floor
    def display_left_wall(self, grid):
        for i in range(HEIGHT - 1):
            grid[i][LEFT_MARGIN] = self.__left_wall
    
    def display_right_wall(self, grid):
        for i in range(HEIGHT - 1):
            grid[i][WIDTH-1] = self.__right_wall

    # Function to create the ceil
    def display_ceil(self, grid):
        for i in range(LEFT_MARGIN, WIDTH - 1):
            grid[0][i] = self.__ceil
