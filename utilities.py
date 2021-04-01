from headers import *
from os import *

# importing classes
from board import Board
from paddle import Paddle
from enemy import Enemy
from brick import Brick
from bomb import Bomb
from ball import Ball
from powerup import PowerUp
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

# The enemy
enemy_obj = Enemy(0, 30)

# Moving balls
ball_obj_array = [Ball(0, 0)]

# Powerups
powerup_obj_array = [PowerUp(0, 0) for i in range(40)]

SHOOT_TIME = [0]

BOMB_TIME = [0]
START_BOMB_FLAG = [0] 

def bricks_fallen():
    os.system('clear')
    game_over()
    print()
    print(Fore.MAGENTA+Style.BRIGHT+"Better Luck next time!".center(SCREEN)+Style.RESET_ALL)
    print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE[0])).center(SCREEN)+Style.RESET_ALL)
    quit()

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
# unbreak_list = [3, 9, 31]
rainbow_list = [0, 30]

def put_brick(ind, row, col_start):
    brick_obj_array[ind].clear(board_obj.grid, brick_obj_array[ind].getx(), brick_obj_array[ind].gety())
    if brick_obj_array[ind].get_value() == '*' or brick_obj_array[ind].get_value() == 'X':
        if row >= HEIGHT-3:
            bricks_fallen()
    elif  brick_obj_array[ind].get_value() > 0 and row >= HEIGHT-3:
        bricks_fallen()
    if ( ind == rainbow_list[0] and RAINBOW_FLAG[0] == 1 )or ( ind == rainbow_list[1] and RAINBOW_FLAG[0] == 1 ):
        brick_obj_array[ind].set_value(random.choice([1, 2, 3]))
    brick_obj_array[ind].show(board_obj.grid, row, col_start)

# LEVEL 1
def place_bricks_lvl1(shift):
    col_start = LEFT_MARGIN + 17
    row_start = HEIGHT - 15 + shift
    ind = 0
    
    for colseg in range(0, 3):
        for row in range(row_start, row_start + 1):
            if L1_ENTER[0] == 0:
                brick_obj_array[ind].reset(board_obj.grid, row, col_start)
            put_brick(ind, row, col_start)
            ind += 1
        col_start += 9
    for colseg in range(3, 6):
        for row in range(row_start, row_start + 1):
            if L1_ENTER[0] == 0:
                brick_obj_array[ind].reset(board_obj.grid, row, col_start)
            put_brick(ind, row, col_start)
            ind += 1
        col_start += 9
    if L1_ENTER[0] == 0:
        for ii in range(ind, 36):
            brick_obj_array[ii].set_gone(1)
    L1_ENTER[0] = 1

# LEVEL 2
def place_bricks_lvl2(shift):
    col_start = LEFT_MARGIN + 17
    row_start = HEIGHT - 30 + shift
    ind = 0
    
    for colseg in range(0, 3):
        for row in range(row_start, row_start + 1):
            if L2_ENTER[0] == 0:
                brick_obj_array[ind].reset(board_obj.grid, row, col_start)
            put_brick(ind, row, col_start)
            ind += 1
        col_start += 9
        if colseg != 2:
            row_start += 2

    for colseg in range(3, 6):
        for row in range(row_start, row_start + 1):
            if L2_ENTER[0] == 0:
                brick_obj_array[ind].reset(board_obj.grid, row, col_start)
            put_brick(ind, row, col_start)
            ind += 1
        row_start -= 2
        col_start += 9
    if L2_ENTER[0] == 0:
        for ii in range(ind, 36):
            brick_obj_array[ii].set_gone(1)
    L2_ENTER[0] = 1
    
# LEVEL 3
def place_bricks_lvl3(shift):
    col_start = LEFT_MARGIN + 17
    row_start = HEIGHT - 30 + shift
    ind = 0
    unbreak_list = []
    if PLACED[0] == 0:
        unbreak_list = random.sample(tot_expbreak_list, 3)
        PLACED[0] = 1

    for colseg in range(0, 3):
        for row in range(row_start, row_start + 6):
            if L3_ENTER[0] == 0:
                brick_obj_array[ind].reset(board_obj.grid, row, col_start)
            if ind in explode_list:
                brick_obj_array[ind].set_value('*')
            if ind in unbreak_list:
                brick_obj_array[ind].set_value('X')
            put_brick(ind, row, col_start)
            ind += 1
        col_start += 9
        if colseg != 2:
            row_start += 1

    for colseg in range(3, 6):
        for row in range(row_start, row_start + 6):
            if L3_ENTER[0] == 0:
                brick_obj_array[ind].reset(board_obj.grid, row, col_start)
            if ind in explode_list:
                brick_obj_array[ind].set_value('*')
            if ind in unbreak_list:
                brick_obj_array[ind].set_value('X')
            put_brick(ind, row, col_start)
            ind += 1
        row_start -= 1
        col_start += 9
    if L3_ENTER[0] == 0:
        for ii in range(ind, 36):
            brick_obj_array[ii].set_gone(1)
    L3_ENTER[0] = 1

# LEVEL 4
def place_bricks_lvl4(shift):
    col_start = LEFT_MARGIN + 17
    row_start = HEIGHT - 15 + shift
    ind = 1
    
    for colseg in range(0, 2):
        for row in range(row_start, row_start + 1):
            if L1_ENTER[0] == 0:
                brick_obj_array[ind].reset(board_obj.grid, row, col_start)
            put_brick(ind, row, col_start)
            brick_obj_array[ind].set_value('X')
            ind += 1
        col_start += 9
    for colseg in range(4, 6):
        for row in range(row_start, row_start + 1):
            if L1_ENTER[0] == 0:
                brick_obj_array[ind].reset(board_obj.grid, row, col_start)
            put_brick(ind, row, col_start)
            brick_obj_array[ind].set_value('X')
            ind += 1
        col_start += 9
    if L4_ENTER[0] == 0:
        for ii in range(ind, 36):
            brick_obj_array[ii].set_gone(1)
    L4_ENTER[0] = 1

def place_bricks(shift):
    if LEVEL[0] == 1:
        place_bricks_lvl1(shift)
    elif LEVEL[0] == 2:
        place_bricks_lvl2(shift)
    elif LEVEL[0] == 3:
        place_bricks_lvl3(shift)
    else:
        place_bricks_lvl4(shift)

def clear_bricks():
    for i in range(0, 36):
        xx = brick_obj_array[i].getx()
        yy = brick_obj_array[i].gety()
        brick_obj_array[i].clear(board_obj.grid, xx, yy)

# Moves the paddle
def move_paddle(newtime):
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

    if char == 'n':
        LEVEL[0] += 1
        SHIFT[0] = 0
        START_LVL[0] = newtime
        SHOOT_FLAG[0] = 0
        ball_obj_array[0].clear(board_obj.grid)
        GRAB_FLAG[0] = 1
        RAINBOW_FLAG[0] = 1
        RAINBOW_FLAG[1] = 1
        place_ball(0)
        clear_bricks()

# Create powerups
def create_powerup(x, y):
    for powerup in powerup_obj_array:
        if powerup.get_status() == 0:
            powerup.start_pos(board_obj.grid, x, y)
            powerup.set_status(1)
            break

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

                if(LEVEL[0] == 4):
                    if ball.handle_ball_enemy_collision(enemy_obj.getxl(), enemy_obj.getxr(), ballx, bally) == 1:
                        ENEMY_HEALTH[0] -= 1
                ball.handle_ball_paddle_collision(paddle_obj.getxl(), paddle_obj.getxr(), ballx, bally)
                ball.handle_ball_wall_collision(ballx, bally)
                indx = 0
                for brick in brick_obj_array:
                    if brick.get_gone() == 0:
                        brickx = brick.getx()
                        bricky = brick.gety()
                        
                        if ball.handle_ball_brick_collision(brickx, bricky, ballx, bally) == 1:
                            if indx == rainbow_list[0]:
                                RAINBOW_FLAG[0] = 0
                            elif indx == rainbow_list[1]:
                                RAINBOW_FLAG[1] = 0

                            if brick.get_value() != 'X' and brick.get_value() != '*':
                                brick.dec_value() 
                                if brick.get_value() == 0:
                                    os.system('aplay -q ./sounds/sound_collide.wav&')
                                    SCORE[0] += 1
                                    xx = brick.getx()
                                    yy = brick.gety()
                                    brick.clear(board_obj.grid, xx, yy)
                                    brick.set_gone(1)
                                    brick.set_value(0)
                                    create_powerup(xx, yy)
                            if brick.get_value() == '*':
                                os.system('aplay -q ./sounds/sound_collide.wav&')
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
                    indx += 1

                nextx = ball.getx() + BALL_SPEED * ball.dirx
                nexty = ball.gety() + BALL_SPEED * ball.diry

                ball.handle_ball_paddle_collision(paddle_obj.getxl(), paddle_obj.getxr(), nextx, nexty)
                ball.handle_ball_wall_collision(nextx, nexty)
                
                if(LEVEL[0] == 4):
                    if ball.handle_ball_enemy_collision(enemy_obj.getxl(), enemy_obj.getxr(), nextx, nexty) == 1:
                        ENEMY_HEALTH[0] -= 1
                indx = 0
                for brick in brick_obj_array:
                    if brick.get_gone() == 0:
                        brickx = brick.getx()
                        bricky = brick.gety()
                        
                        if ball.handle_ball_brick_collision(brickx, bricky, nextx, nexty) == 1:
                            if brick.get_value() != 'X' and brick.get_value() != '*':
                                if indx == rainbow_list[0]:
                                    RAINBOW_FLAG[0] = 0
                                elif indx == rainbow_list[1]:
                                    RAINBOW_FLAG[1] = 0
                                brick.dec_value() 
                                if brick.get_value() == 0:
                                    os.system('aplay -q ./sounds/sound_collide.wav&')
                                    SCORE[0] += 1
                                    xx = brick.getx()
                                    yy = brick.gety()
                                    brick.clear(board_obj.grid, xx, yy)
                                    brick.set_gone(1)
                                    brick.set_value(0)
                                    create_powerup(xx, yy)
                            if brick.get_value() == '*':
                                os.system('aplay -q ./sounds/sound_collide.wav&')
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
                    indx += 1            
                
                ball.move(board_obj.grid)
    return NUM_BALLS

# powerups

bullet_obj_array = [Ball(0, 0) for i in range(40)]

def shoot_bullets():
    num = 0
    for bullet in bullet_obj_array:
        if num == 2:
            break
        if bullet.get_status() == 0 and num == 0:
            num += 1
            bullet.set_dirx(0)
            bullet.set_diry(-1)
            bullet.start_shoot(board_obj.grid, paddle_obj.getxl(), HEIGHT-4)
            bullet.set_status(1)
        if bullet.get_status() == 0 and num == 1:
            num += 1
            bullet.set_dirx(0)
            bullet.set_diry(-1)
            bullet.start_shoot(board_obj.grid, paddle_obj.getxr(), HEIGHT-4)
            bullet.set_status(1)

def move_bullets():
    for bullet in bullet_obj_array:
        bulletx = bullet.getx()
        bullety = bullet.gety()

        if bullet.handle_ball_wall_collision(bulletx, bullety) == 1 and bullet.get_status() == 1:
            bullet.clear(board_obj.grid)
            bullet.set_status(0)
        if bullet.has_fallen(board_obj.grid) == 1 and bullet.get_status() == 1:
            bullet.clear(board_obj.grid)
            bullet.set_status(0)
        if(LEVEL[0] == 4):
            if bullet.handle_ball_enemy_collision(enemy_obj.getxl(), enemy_obj.getxr(), bulletx, bullety) == 1:
                ENEMY_HEALTH[0] -= 1
                bullet.clear(board_obj.grid)
                bullet.set_status(0)
        indx = 0
        for brick in brick_obj_array:
            if brick.get_gone() == 0:
                brickx = brick.getx()
                bricky = brick.gety()
                
                if bullet.handle_ball_brick_collision(brickx, bricky, bulletx, bullety) == 1 and bullet.get_status() == 1:
                    bullet.clear(board_obj.grid)
                    bullet.set_status(0)
                    if indx == rainbow_list[0]:
                        RAINBOW_FLAG[0] = 0
                    elif indx == rainbow_list[1]:
                        RAINBOW_FLAG[1] = 0

                    if brick.get_value() != 'X' and brick.get_value() != '*':
                        brick.dec_value() 
                        if brick.get_value() == 0:
                            os.system('aplay -q ./sounds/sound_collide.wav&')
                            SCORE[0] += 1
                            xx = brick.getx()
                            yy = brick.gety()
                            brick.clear(board_obj.grid, xx, yy)
                            brick.set_gone(1)
                            brick.set_value(0)
                            create_powerup(xx, yy)
                    if brick.get_value() == '*':
                        os.system('aplay -q ./sounds/sound_collide.wav&')
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
            indx += 1
        if bullet.get_status() == 1:
            bullet.move(board_obj.grid)
    

def move_powerups(newtime):
    for powerup in powerup_obj_array:
        if powerup.on_paddle(board_obj.grid, paddle_obj.getxl(), paddle_obj.getxr(), powerup.getx(), powerup.gety()) == 1 and powerup.get_status() == 1:
            powerup.set_status(0)
            powerup.clear(board_obj.grid)
            SHOOT_FLAG[0] = 1
            SHOOT_TIME[0] = newtime
            END_SHOOT[0] = newtime + POWERUP_LIFE[0]
        elif powerup.gety() < HEIGHT - 4 and powerup.get_status() == 1:
            powerup.move(board_obj.grid)
        else:
            powerup.set_status(0)
            powerup.clear(board_obj.grid)

def execute_powerups(newtime):
    if newtime > END_SHOOT[0]:
        SHOOT_FLAG[0] = 0
    if SHOOT_FLAG[0] == 1:
        if newtime == SHOOT_TIME[0]:
            shoot_bullets()
            SHOOT_TIME[0] += 2


# Moves the enemy

def shoot_bomb(left, right):
    num = 0
    for bomb in bomb_obj_array:
        if num == 1:
            break
        if bomb.get_status() == 0 and num == 0:
            num += 1
            bomb.start_pos(board_obj.grid, left, right)
            bomb.set_status(1)

def move_enemy(newtime):
    enemy_obj.show(board_obj.grid, paddle_obj.getxl(), paddle_obj.getxr())
    if START_BOMB_FLAG[0] == 0:
        shoot_bomb(enemy_obj.getxl(), enemy_obj.getxr())
        START_BOMB_FLAG[0] = 1
        BOMB_TIME[0] = newtime
    if newtime == BOMB_TIME[0]:
        shoot_bomb(enemy_obj.getxl(), enemy_obj.getxr())
        BOMB_TIME[0] += 3

# bomb
bomb_obj_array = [Bomb(0, 0) for i in range(40)]

def move_bombs(newtime):
    for bomb in bomb_obj_array:
        if bomb.on_paddle(board_obj.grid, paddle_obj.getxl(), paddle_obj.getxr(), bomb.getx(), bomb.gety()) == 1 and bomb.get_status() == 1:
            bomb.set_status(0)
            bomb.clear(board_obj.grid)
            BOMB_TIME[0] = newtime
            LIVES[0] -= 1
        elif bomb.gety() < HEIGHT - 4 and bomb.get_status() == 1:
            bomb.move(board_obj.grid)
        else:
            bomb.set_status(0)
            bomb.clear(board_obj.grid)