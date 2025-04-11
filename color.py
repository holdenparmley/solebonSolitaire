import os

WHITE = 7
BLACK = 0
GREEN = 2
RED = 1

def color(n):
    os.system(f"tput setaf {n}")

def fgcolor(n):
    color(n)

def bgcolor(n):
    os.system(f"tput setab {n}")

def nocolor(n):
    os.system("tput sgr0")
    
