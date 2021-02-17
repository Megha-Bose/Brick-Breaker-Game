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
    newtime = GAMETIME - (round(time.time()) - round(start_time))
    reposition_cursor(0, 0)
    if(LIVES <= 0):
        os.system('clear')
        game_over()
        print()
        if(LIVES <= 0):
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"LIVES OVER.".center(SCREEN)+Style.RESET_ALL)
        print(Fore.MAGENTA+Style.BRIGHT+"Better Luck next time!".center(SCREEN)+Style.RESET_ALL)
        print(Fore.MAGENTA+Style.BRIGHT+str("SCORE: " + str(SCORE)).center(SCREEN)+Style.RESET_ALL)
        quit()
    place_bricks()
    board_obj.print_board()
    move_paddle()
    move_balls()

    signal.signal(signal.SIGINT, handler)
    