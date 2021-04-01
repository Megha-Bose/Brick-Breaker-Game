from headers import *
from utilities import * 

# Start time of the game
start_time = time.time()
screen_time = time.time()

os.system('clear')
place_bricks(0)
place_ball(0)

def handler(signum, frame):
    os.system('clear')
    sys.exit(0)

while True:
    signal.signal(signal.SIGINT, handler)
    newtime = (round(time.time()) - round(start_time))
    reposition_cursor(0, 0)
    if LIVES[0] <= 0 and SCORE[0] < 1000:
        os.system('clear')
        game_over()
        print()
        if(LIVES[0] <= 0 ):
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"LIVES OVER.".center(SCREEN)+Style.RESET_ALL)
        print(Fore.MAGENTA+Style.BRIGHT+"Better Luck next time!".center(SCREEN)+Style.RESET_ALL)
        print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE[0])).center(SCREEN)+Style.RESET_ALL)
        quit()

    elif LEVEL[0] > 4:
        os.system('clear')
        escape()
        print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE[0]) + " | TIME TAKEN: " + str(newtime)).center(SCREEN)+Style.RESET_ALL)
        quit()

    elif(ENEMY_HEALTH[0] == 0 and LEVEL[0] == 4):
        os.system('clear')
        SCORE[0] == 1000
        win()
        print()
        print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE[0]) + " | TIME TAKEN: " + str(newtime)).center(SCREEN)+Style.RESET_ALL)
        quit()

    elif(SCORE[0] == 48 and LEVEL[0] == 3):
        os.system('clear')
        LEVEL[0] += 1
        START_LVL[0] = newtime
        SHOOT_FLAG[0] = 0
        RAINBOW_FLAG[0] = 1
        RAINBOW_FLAG[1] = 1
        print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE[0]) + " | TIME TAKEN: " + str(newtime)).center(SCREEN)+Style.RESET_ALL)

    elif(SCORE[0] == 12 and LEVEL[0] == 2):
        os.system('clear')
        LEVEL[0] += 1
        START_LVL[0] = newtime
        SHOOT_FLAG[0] = 0
        RAINBOW_FLAG[0] = 1
        RAINBOW_FLAG[1] = 1
        print(Fore.MAGENTA+Style.BRIGHT+str("LEVEL: " + str(LEVEL[0]) + " | SCORE: " + str(SCORE[0]) + " | LIVES LEFT: " + str(LIVES[0]) + " | TIME: " + str(newtime)).center(SCREEN)+Style.RESET_ALL)

    elif(SCORE[0] == 6 and LEVEL[0] == 1):
        os.system('clear')
        LEVEL[0] += 1
        START_LVL[0] = newtime
        SHOOT_FLAG[0] = 0
        RAINBOW_FLAG[0] = 1
        RAINBOW_FLAG[1] = 1
        print(Fore.MAGENTA+Style.BRIGHT+str("LEVEL: " + str(LEVEL[0]) + " | SCORE: " + str(SCORE[0]) + " | LIVES LEFT: " + str(LIVES[0]) + " | TIME: " + str(newtime)).center(SCREEN)+Style.RESET_ALL)

    else:
        os.system('clear')
        if LEVEL[0] == 4:
            print(Fore.MAGENTA+Style.BRIGHT+str("ENEMY HEATH: " + ENEMY_HEALTH[0] * str("|X|")).center(SCREEN)+Style.RESET_ALL)
        if SHOOT_FLAG[0] == 1:
            print(Fore.MAGENTA+Style.BRIGHT+str("LEVEL: " + str(LEVEL[0]) + " | SCORE: " + str(SCORE[0]) + " | LIVES LEFT: " + str(LIVES[0]) + " | TIME: " + str(newtime) + " | REM. TIME SHOOT POWERUP : " + str(END_SHOOT[0] - newtime)).center(SCREEN)+Style.RESET_ALL)
        else:
            print(Fore.MAGENTA+Style.BRIGHT+str("LEVEL: " + str(LEVEL[0]) + " | SCORE: " + str(SCORE[0]) + " | LIVES LEFT: " + str(LIVES[0]) + " | TIME: " + str(newtime)).center(SCREEN)+Style.RESET_ALL)

    if newtime - START_LVL[0] < FALL_TIME[0]:
        place_bricks(0)
    else:
        place_bricks(SHIFT[0])
    board_obj.print_board()
    move_paddle(newtime)
    if LEVEL[0] == 4:
        move_enemy(newtime)
        move_bombs(newtime)
    shoot_ball()
    move_balls()
    move_bullets()
    move_powerups(newtime)
    execute_powerups(newtime)

    signal.signal(signal.SIGINT, handler)
    