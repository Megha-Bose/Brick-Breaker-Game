from headers import *
from objects import *
from utilities import *
from os import *

class Bomb(Object):
    # Inherits Object class
    def __init__(self, x, y):
        self.diry = +1
        self.active = 0
        self.__body = np.array([["*"]])
        Object.__init__(self, x, y)
    
    def get_status(self):
        return self.active
    
    def set_status(self, status):
        self.active = status
    
    # Function to place the bomb randomly on the paddle at each start
    def start_pos(self, grid, left, right):
        self.setx((left + right) // 2)
        self.sety(4)
        grid[3][self.getx()] = self.__body[0][0]
    
    # Check if bomb has gone below paddle
    def has_fallen(self, grid):
        y = self.gety()
        if y > HEIGHT - 4:
            self.clear(grid)
            return 1
        return 0
    
    # Check if bomb is on paddle 
    def on_paddle(self, grid, paddle_xl, paddle_xr, bomb_x, bomb_y):
        if bomb_x >= paddle_xl and bomb_x <= paddle_xr and bomb_y == HEIGHT - 4:
            self.clear(grid)
            return 1
        return 0

    # Clearing the position of the bomb as it moves
    def clear(self, grid):
        x = self.getx()
        y = self.gety()
        grid[y][x] = ' '
            
    # Updating position of bomb
    def show(self, grid, x, y):
        self.clear(grid)
        self.setx(x)
        self.sety(y)
        grid[y][x] = self.__body[0][0]
    
    # Moving in given direction from current position
    def move(self, grid):
        nexty = self.gety() + +BOMB_SPEED[0]
        self.show(grid, self.getx(), nexty)


