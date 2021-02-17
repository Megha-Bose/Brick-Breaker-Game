from headers import *
from objects import *

class Paddle(Object):

    # Inherits Object class
    def __init__(self, x_coor, y_coor):
        # self.__body = np.array([["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]])
        # self.__long_body = np.array([["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]])
        # self.__short_body = np.array([["_", "_", "_", "_", "_", "_", "_", "_"]])
        self.xl = x_coor
        self.xr = x_coor + 12
        Object.__init__(self, x_coor, y_coor)

    def getxl(self):
        return self.xl

    def getxr(self):
        return self.xr

    def setxl(self, xl):
        self.xl = xl

    def setxr(self, xr):
        self.xr = xr
    
    # Setting start position of paddle
    def start_pos(self, grid):
        for j in range(self.getxl(), self.getxr() + 1):
            grid[HEIGHT-3][j]=self.__body[0][j-x]

    # Clearing the position of paddle as we move it
    def clear(self, grid):
        xl = self.getxl()
        xr = self.getxr()
        for j in range(xl, xr + 1):
            grid[HEIGHT-3][j]=' '
            
    # Showing paddle as it moves
    def show(self, grid, xl, xr):
        self.clear(grid)
        self.setxl(xl)
        self.setxr(xr)
        for j in range(xl, xr + 1):
            grid[HEIGHT-3][j] = str(Fore.BLACK + Back.WHITE + Style.BRIGHT + ' ' + Style.RESET_ALL)