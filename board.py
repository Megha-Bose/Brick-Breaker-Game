from headers import *

class Board:
    # Creates the board for the game

    # Constructor function
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.grid = []
        self.__flag = 0

    # Function to create the playing board
    def create_board(self):
        for i in range(self.__rows):
            self.box = []
            for j in range(self.__cols):
                self.box.append(" ")
            self.grid.append(self.box)
        

    # Function to print the playing board
    def print_board(self):
            for i in range(self.__rows):
                for j in range (0, self.__cols):
                    print(self.grid[i][j], end = '')    
                print()
