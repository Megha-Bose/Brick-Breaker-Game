import time, os, sys
import numpy as np
import signal
import random
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from colorama import init, Fore, Back, Style
init()

HEIGHT=40
WIDTH=90
PADDLE_LEN = 10
INPUT_CHAR=''
LIVES = [20]
LEVEL = [1]
SCORE = [0]
START = [0]
START_LVL = [0]
FALL_TIME = [4]
SHIFT = [0]
GAMETIME = 100
LEFT_MARGIN = 10
BALL_SPEED = 1
PLACED = [0]

MULTI_BALL = 2
GRAB_FLAG = [1]
SHOOT_FLAG = [0]
END_SHOOT = [0]
EXP_PAD_FLAG = 0
SHR_PAD_FLAG = 0
BALL_X_FLAG = 0
FAST_BALL_FLAG = 0
THRU_BALL_FLAG = 0
SCREEN = 100
RAINBOW_FLAG = [1, 1]

L1_ENTER = [0]
L2_ENTER = [0]
L3_ENTER = [0]
L4_ENTER = [0]

NUM_BALLS = [1]
POWERUP_LIFE = [6]
POWERUP_SPEED = [1]
BOMB_SPEED = [1]
ENEMY_HEALTH = [5]

def reposition_cursor(x, y):
    print("\033[%d;%dH" % (x, y))

# POWER UPS:
EXP_PAD = Fore.LIGHTGREEN_EX + "+" + Fore.RESET
SHR_PAD = Fore.LIGHTMAGENTA_EX + "-" + Fore.RESET
BALL_X = Fore.LIGHTWHITE_EX + "x" + Fore.RESET
FAST_BALL = Fore.LIGHTYELLOW_EX + "*" + Fore.RESET
THRU_BALL = Fore.LIGHTCYAN_EX + "$" + Fore.RESET
GRAB = Fore.LIGHTWHITE_EX + "&" + Fore.RESET

def win():
    os.system('aplay -q ./sounds/sound_win.wav&')
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " __     __                                      ___".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " \ \   / /                                      | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  \ \_/ /_  __  __    _  ___  _  ____  _ ___    | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "   \   / _ \| | | |  | | | | | |/___ \| |__ \   | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    | | (_| | |_| |  | |_| |_| | |__| | |  | |  |_|".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    |_|\___/\_____/   \__,__,__/\____/|_|  |_|  (_)".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                   ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                   ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                   ".center(SCREEN)+Style.RESET_ALL)   

def escape():
    os.system('aplay -q ./sounds/sound_game_over.wav&')
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " __     __                            _    _    ___".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " \ \   / /                           |_| _| |_  | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  \ \_/ /_  __  __    _____   _  ___  _ /_   _\ | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "   \   / _ \| | | |  |  _  | | | | | | |  | |   | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    | | (_| | |_| |  | |_| | | |_| | | |  | |   |_|".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    |_|\___/\_____/   \__, ,  \___/  |_|  |_|   (_)".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                         | |                       ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                         |_|                       ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                   ".center(SCREEN)+Style.RESET_ALL)      

def game_over():
    os.system('aplay -q ./sounds/sound_game_over.wav&')
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                      ".center(SCREEN))                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  _____                          ____                 ".center(SCREEN))                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " / ____|                        / __ \                ".center(SCREEN))              
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "| |  __  __ _ _ __ ___   ___   | |  | |_   _____ _ __ ".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"| | |_ |/ _` | '_ ` _ \ / _ \  | |  | \ \ / / _ \ '__|".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"| |__| | (_| | | | | | |  __/  | |__| |\ V /  __/ |   ".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +" \_____|\__,_|_| |_| |_|\___|   \____/  \_/ \___|_|   ".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                      ".center(SCREEN)+Style.RESET_ALL)                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                      ".center(SCREEN)+Style.RESET_ALL)                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                      ".center(SCREEN)+Style.RESET_ALL)      
