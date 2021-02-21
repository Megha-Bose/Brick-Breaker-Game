from headers import *
from objects import *
from utilities import *

class Ball(Object):
    # Inherits Object class
    def __init__(self, x, y):
        self.dirx = -1
        self.diry = -1
        self.__body = np.array([["0"]])
        Object.__init__(self, x, y)

    def dec_lives(self):
        LIVES -= 1

    def inc_score(self, val):
        SCORE += val
    
    # Function to place the ball randomly on the paddle at each start
    def start_pos(self, grid, paddle_xl, paddle_xr):
        xpos = random.randrange(paddle_xl, paddle_xr + 1)
        self.setx(xpos)
        self.sety(HEIGHT-4)
        grid[HEIGHT-4][xpos] = self.__body[0][0]
    
    # Check if ball has gone below paddle
    def has_fallen(self, grid):
        y = self.gety()
        if y > HEIGHT - 4:
            NUM_BALLS[0] -= 1
            return 1
        return 0
    
    # Check if ball in on paddle 
    def on_paddle(self, grid, paddle_xl, paddle_xr):
        ball_x = self.getx()
        if ball_x >= paddle_xl and ball_x <= paddle_xr and ball_y == HEIGHT - 4:
            return 1
        return 0

    # Clearing the position of the ball as it moves
    def clear(self, grid):
        x = self.getx()
        y = self.gety()
        grid[y][x] = ' '
            
    # Updating position of ball
    def show(self, grid, x, y):
        self.clear(grid)
        self.setx(x)
        self.sety(y)

        grid[y][x] = self.__body[0][0]
    
    # Moving in given direction from current position
    def move(self, grid):
        nextx = self.getx() + BALL_SPEED * self.dirx
        nexty = self.gety() + BALL_SPEED * self.diry
        self.show(grid, nextx, nexty)

    # Handling ball-paddle collision
    def handle_ball_paddle_collision(self, padxl, padxr, x, y):
        if x >= padxl and x <= padxr and y == HEIGHT - 3:
            if (x >= padxl and x <= padxl + 2) and (self.dirx == 0):
                self.dirx = -1
            if (x >= padxr - 2 and x <= padxr) and (self.dirx == 0):
                self.dirx = 1
            else:
                self.diry = -self.diry
            return 1
        return 0

    # Handling ball-wall collision
    def handle_ball_wall_collision(self, x, y):
        if x == LEFT_MARGIN or x == WIDTH - 1:
            self.dirx = -self.dirx
            return 1
        if y == 0:
            self.diry = -self.diry
            return 1
        return 0

    # Handling ball-brick collision
    def handle_ball_brick_collision(self, brickx, bricky, x, y):
        if (x == brickx or x == brickx + 9) and y == bricky:
            self.dirx = -self.dirx
            self.diry = -self.diry
            return 1
        elif x > brickx and x < brickx + 9 and y == bricky:
            self.diry = -self.diry
            return 1
        else:
            return 0

