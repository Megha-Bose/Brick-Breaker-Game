import time
import numpy as np
import signal
import random
import os
import sys
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from colorama import init, Fore, Back, Style
init()

HEIGHT=50
WIDTH=114
PADDLE_LEN = 12
INPUT_CHAR=''
LIVES = 10
BRICKS = 36
SCORE = 0
GAMETIME = 100
LEFT_MARGIN = 10
NUM_BALLS = 1
BALL_SPEED = 1

MULTI_BALL = 2
GRAB_FLAG = 0
EXP_PAD_FLAG = 0
SHR_PAD_FLAG = 0
BALL_X_FLAG = 0
FAST_BALL_FLAG = 0
THRU_BALL_FLAG = 0
SCREEN = 200

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
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " __     __                                      ___".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " \ \   / /                                      | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  \ \_/ /_  __  __    _  ___  _  ____  _ ___    | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "   \   / _ \| | | |  | | | | | |/___ \| |__ \   | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    | | (_| | |_| |  | |_| |_| | |__| | |  | |  |_|".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    |_|\___/\_____/   \__,__,__/\____/|_|  |_|  (_)".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                   ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                   ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                   ".center(SCREEN)+Style.RESET_ALL)      

def game_over():
    os.system('aplay -q ./sounds/game_over.wav&')
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
