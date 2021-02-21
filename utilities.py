from headers import *

# importing classes
from board import Board
from paddle import Paddle
from brick import Brick
from ball import Ball
from background import Background

# The board
board_obj = Board(HEIGHT, WIDTH)
board_obj.create_board()

# The background
bg_obj = Background()
bg_obj.display_ceil(board_obj.grid)
bg_obj.display_left_wall(board_obj.grid)
bg_obj.display_right_wall(board_obj.grid)

# The paddle
paddle_obj = Paddle(0, 0)
paddle_obj.show(board_obj.grid, int(WIDTH / 2), int(WIDTH / 2) + PADDLE_LEN)

# Moving balls
ball_obj_array = [Ball(0, 0)]

def print_header(newtime):
    print(Fore.WHITE + Back.BLACK_EX + Style.BRIGHT + "               ".center(SCREEN) + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLACK_EX + Style.BRIGHT + "THE BRICK BREAKER".center(SCREEN) + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLACK_EX+ Style.BRIGHT + "               ".center(SCREEN) + Style.RESET_ALL)
    stats = str("LIVES: " + str(paddle_obj.show_lives()) + "  |  SCORE: " + SCORE + "  |  TIME: " + str(newtime))
    print(Fore.WHITE + Back.BLACK_EX + Style.BRIGHT + stats.center(SCREEN))
    print(Fore.WHITE + Back.BLACK_EX + Style.BRIGHT + "               ".center(SCREEN) + Style.RESET_ALL)

# Placing bricks
brick_obj_array = [Brick(0, 0) for i in range(36)]

PLACED = [0]
explode_list = [7, 8, 12, 13, 18, 19, 25, 26]
tot_expbreak_list = [1, 2, 3, 4, 6, 9, 14, 20, 24, 27, 31, 32, 33, 34]
    
def place_bricks():
    col_start = LEFT_MARGIN + 17
    row_start = HEIGHT - 30
    ind = 0
    unbreak_list = []
    if PLACED[0] == 0:
        unbreak_list = random.sample(tot_expbreak_list, 6)
        PLACED[0] = 1
    for colseg in range(0, 3):
        for row in range(row_start, row_start + 6):
            if ind in explode_list:
                brick_obj_array[ind].set_value('*')
            if ind in unbreak_list:
                brick_obj_array[ind].set_value('X')
            brick_obj_array[ind].show(board_obj.grid, row, col_start)
            ind += 1
        col_start += 9
        if colseg != 2:
            row_start += 1
            

    for colseg in range(3, 6):
        for row in range(row_start, row_start + 6):
            if ind in explode_list:
                brick_obj_array[ind].set_value('*')
            if ind in unbreak_list:
                brick_obj_array[ind].set_value('X')
            brick_obj_array[ind].show(board_obj.grid, row, col_start)
            ind += 1
        row_start -= 1
        col_start += 9

# Moves the paddle
def move_paddle():
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout = 0.1):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    
    INPUT_CHAR = user_input()
    char = INPUT_CHAR

    if char == 'a':
        paddle_obj.clear(board_obj.grid)
        if paddle_obj.getxl() - 1 >= LEFT_MARGIN and paddle_obj.getxr() - 1 >= LEFT_MARGIN + PADDLE_LEN:
            paddle_obj.setxl(paddle_obj.getxl() - 1)
            if START[0] == 0:
                ball_obj_array[0].show(board_obj.grid, ball_obj_array[0].getx() - 1, ball_obj_array[0].gety())
            paddle_obj.setxr(paddle_obj.getxr() - 1)
        paddle_obj.show(board_obj.grid, paddle_obj.getxl(), paddle_obj.getxr())

    if char == 'd':
        paddle_obj.clear(board_obj.grid)
        if paddle_obj.getxr() + 1 <= WIDTH - 1 and paddle_obj.getxl() + 1 <= WIDTH - 1 - PADDLE_LEN:
            paddle_obj.setxl(paddle_obj.getxl() + 1)
            if START[0] == 0:
                ball_obj_array[0].show(board_obj.grid, ball_obj_array[0].getx() + 1, ball_obj_array[0].gety())
            paddle_obj.setxr(paddle_obj.getxr() + 1)
        paddle_obj.show(board_obj.grid, paddle_obj.getxl(), paddle_obj.getxr())

    if char == 'q':
        quit()


# Ball functions

def place_ball(ind):
    ball_obj_array[ind].start_pos(board_obj.grid, paddle_obj.getxl(), paddle_obj.getxr())
    x = ball_obj_array[ind].getx()
    y = ball_obj_array[ind].gety()
    ball_obj_array[ind].show(board_obj.grid, x, y)

def shoot_ball():
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout = 0.1):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    
    INPUT_CHAR = user_input()
    char = INPUT_CHAR

    if char == 'w':
        GRAB_FLAG[0] = 0
        START[0] = 1

def move_balls():
    for ball in ball_obj_array:
        if GRAB_FLAG[0] != 1 or ball.gety() != HEIGHT - 4:
            if ball.has_fallen(board_obj.grid):
                ball.clear(board_obj.grid)
                if NUM_BALLS[0] == 0:
                    LIVES[0] -= 1
                    ball.start_pos(board_obj.grid, paddle_obj.getxl(), paddle_obj.getxr())
                    NUM_BALLS[0] += 1
            else:
                ballx = ball.getx()
                bally = ball.gety()

                ball.handle_ball_paddle_collision(paddle_obj.getxl(), paddle_obj.getxr(), ballx, bally)
                ball.handle_ball_wall_collision(ballx, bally)
                
                for brick in brick_obj_array:
                    if brick.get_gone() == 0:
                        brickx = brick.getx()
                        bricky = brick.gety()
                        
                        if ball.handle_ball_brick_collision(brickx, bricky, ballx, bally) == 1:
                            if brick.get_value() != 'X' and brick.get_value() != '*':
                                brick.dec_value() 
                                if brick.get_value() == 0:
                                    SCORE[0] += 1
                                    xx = brick.getx()
                                    yy = brick.gety()
                                    brick.clear(board_obj.grid, xx, yy)
                                    brick.set_gone(1)
                                    brick.set_value(0)
                            if brick.get_value() == '*':
                                expbreak_list = tot_expbreak_list + explode_list
                                for br in expbreak_list:
                                    if brick_obj_array[br].get_gone() == 0:
                                        brick_obj_array[br].set_value(0) 
                                        SCORE[0] += 1
                                        xx = brick_obj_array[br].getx()
                                        yy = brick_obj_array[br].gety()
                                        brick_obj_array[br].clear(board_obj.grid, xx, yy)
                                        brick_obj_array[br].set_gone(1)
                                        brick_obj_array[br].set_value(0)

                nextx = ball.getx() + BALL_SPEED * ball.dirx
                nexty = ball.gety() + BALL_SPEED * ball.diry

                ball.handle_ball_paddle_collision(paddle_obj.getxl(), paddle_obj.getxr(), nextx, nexty)
                ball.handle_ball_wall_collision(nextx, nexty)
                
                for brick in brick_obj_array:
                    if brick.get_gone() == 0:
                        brickx = brick.getx()
                        bricky = brick.gety()
                        
                        if ball.handle_ball_brick_collision(brickx, bricky, nextx, nexty) == 1:
                            if brick.get_value() != 'X' and brick.get_value() != '*':
                                brick.dec_value() 
                                if brick.get_value() == 0:
                                    SCORE[0] += 1
                                    xx = brick.getx()
                                    yy = brick.gety()
                                    brick.clear(board_obj.grid, xx, yy)
                                    brick.set_gone(1)
                                    brick.set_value(0)
                            if brick.get_value() == '*':
                                expbreak_list = tot_expbreak_list + explode_list
                                for br in expbreak_list:
                                    if brick_obj_array[br].get_gone() == 0:
                                        brick_obj_array[br].set_value(0) 
                                        SCORE[0] += 1
                                        xx = brick_obj_array[br].getx()
                                        yy = brick_obj_array[br].gety()
                                        brick_obj_array[br].clear(board_obj.grid, xx, yy)
                                        brick_obj_array[br].set_gone(1)
                                        brick_obj_array[br].set_value(0)
                                
                
                ball.move(board_obj.grid)
    return NUM_BALLS
