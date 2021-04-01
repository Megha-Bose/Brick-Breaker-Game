from headers import *
from objects import *

class Enemy(Object):

    # Inherits Object class
    def __init__(self, x_coor, y_coor):
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

    # Clearing the position of enemy as we move it
    def clear(self, grid):
        xl = self.getxl()
        xr = self.getxr()
        for j in range(xl, xr + 1):
            grid[3][j]=' '
            
    # Showing enemy as it moves
    def show(self, grid, xl, xr):
        self.clear(grid)
        self.setxl(xl)
        self.setxr(xr)
        for j in range(xl, xr + 1):
            grid[3][j] = str(Fore.WHITE + Back.RED + Style.BRIGHT + 'O' + Style.RESET_ALL)