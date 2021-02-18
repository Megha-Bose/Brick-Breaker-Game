from headers import *
from utilities import * 

# Start time of the game
start_time = time.time()
screen_time = time.time()

os.system('clear')
place_bricks()
place_ball(0)

def handler(signum, frame):
    os.system('clear')
    sys.exit(0)

while True:
    signal.signal(signal.SIGINT, handler)
    newtime = (round(time.time()) - round(start_time))
    reposition_cursor(0, 0)
    if LIVES[0] <= 0 and SCORE[0] < BRICKS:
        os.system('clear')
        game_over()
        print()
        if(LIVES[0] <= 0):
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"LIVES OVER.".center(SCREEN)+Style.RESET_ALL)
        print(Fore.MAGENTA+Style.BRIGHT+"Better Luck next time!".center(SCREEN)+Style.RESET_ALL)
        print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE[0])).center(SCREEN)+Style.RESET_ALL)
        quit()
    elif(SCORE[0] == BRICKS):
        os.system('clear')
        win()
        print()
        print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE[0]) + " | TIME TAKEN: " + str(newtime)).center(SCREEN)+Style.RESET_ALL)
        quit()
    else:
        print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE[0]) + " | LIVES LEFT: " + str(LIVES[0]) + " | TIME: " + str(newtime)).center(SCREEN)+Style.RESET_ALL)

    place_bricks()
    board_obj.print_board()
    move_paddle()
    move_balls()

    signal.signal(signal.SIGINT, handler)
    