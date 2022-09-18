import random
import time
from math import exp
import os
from turtle import color
import requests
import sys
from pystyle import Colors, Colorate , Write, Colors
from colorama import Fore
from selenium import webdriver
os.system(f'cls & mode 120,30 & title VastVccGen(V1.2)')


# colors
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"


Write.Input("""


██╗░░░██╗░█████╗░░██████╗████████╗  ░█████╗░░█████╗░
██║░░░██║██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗
╚██╗░██╔╝███████║╚█████╗░░░░██║░░░  ██║░░╚═╝██║░░╚═╝
░╚████╔╝░██╔══██║░╚═══██╗░░░██║░░░  ██║░░██╗██║░░██╗
░░╚██╔╝░░██║░░██║██████╔╝░░░██║░░░  ╚█████╔╝╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░  ░╚════╝░░╚════╝░
                                                                                                  
          Made By Vast#4441
          [1]VCC Generator
          [2]Promo Link Generator [PAID]
          Select Option -> """,Colors.red_to_purple, interval=0.0095)
while True:
    exp_date2 = str(random.randint(1, 12))
    if exp_date2 == str(1):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(2):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(3):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(4):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(5):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(6):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(7):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(8):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(9):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(10):
        pass
    elif exp_date2 == str(11):
        pass
    elif exp_date2 == str(12):
        pass

    card = "5239 95" + str(random.randint(10, 99)) + " " + str(random.randint(1000, 9999)) + " " + str(random.randint(1000, 9999)) + " | " + exp_date2 + "/"  + str(random.randint(23, 29)) + " | " + str(random.randint(100, 999))
    f = open('CC.txt', "a+")
    f.write(f'{card}\n')
    f.close()

    Write.Input(f"[GENERATED] - {card}",Colors.green_to_white,interval=0.0000001)
    time.sleep(0.025)