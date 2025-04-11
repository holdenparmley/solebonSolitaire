# starter code for solitaitre card game assingment

# v 0.04

# v 0.01 initial version
# v 0.02 fixed to shuffle to work with any size deck
# v 0.03 made cardFromName slightly more robust
# v 0.04 changed card back graphic from [#] to [_]
import random

import color
from color import fgcolor
from color import bgcolor

pips = ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ']
suit = ['♠', '♦', '♥', '♣']
back = "[_]"

def fresh_deck():
    deck = []
    for i in range(0, 52):
        deck.append(i)
    return deck    


def shuffle(deck):
    for i in range (len(deck)-1, 0, -1):
        r = random.randint(0, i)
        deck[i], deck[r] = deck[r], deck[i]

# cards in 0-51, -1 for a blank card-sized space
def print_card(card, show = True):
    bgcolor(color.GREEN)
    print(" ", end="", flush=True)
    if (card == -1):
        bgcolor(color.GREEN)
        fgcolor(color.BLACK)
        print("[    ]", end="", flush= True)
        return
    if (show == False):
        bgcolor(color.WHITE)
        fgcolor(color.BLACK)
        print(back, end="", flush= True)
        bgcolor(color.GREEN)
        print(" ", end="", flush=True)
        return
    n = card % 13
    s = card // 13
    bgcolor(color.WHITE)
    if (s == 0 or s == 3):
        fgcolor(color.BLACK)
    else:
        fgcolor(color.RED)
    print(f"{suit[s]}{pips[n]}", end="", flush=True)  
    fgcolor(color.BLACK)
    bgcolor(color.GREEN)
    print(" ", end="", flush=True)


# print a blank space where a card could exist
def print_blank():
    bgcolor(color.GREEN)
    print("     ", end="", flush=True)

# returns True if a card is an ace
def isAce(card):
    aces = [0, 13, 26, 39]
    return (card in aces)

# returns True if a card is a king
def isKing(card):
    kings = [12, 25, 38, 51]
    return (card in kings)

# returns one lower
def prevCard(card):
    return (card-1)

# returns one higher
def nextCard(card):
    return (card+1)

# main
def main():
    deck = fresh_deck()
    bgcolor(color.GREEN)
    print("", flush=True)

    col_count = 0;
    row = 0
    for card in deck:
        if (col_count == 7):
            bgcolor(color.GREEN)
            print("", flush=True)
            col_count = 0
            row = row + 1
        if (row < 3 ):
            print_card(card, False)
        else:    
            print_card(card)
        col_count = col_count + 1
    bgcolor(color.GREEN)
    print("", flush=True)
    print("", flush=True)
    print("", flush=True)
    


    shuffle(deck)



    col_count = 0;
    row = 0
    for card in deck:
        if (col_count == 7):
            bgcolor(color.GREEN)
            print("", flush=True)
            col_count = 0
            row = row + 1
        if (row < 2):
            print_card(card, False)
        else:    
            print_card(card)
        col_count = col_count + 1
    bgcolor(color.GREEN)
    print("", flush=True)

def pipsFromCard(card):
    return card % 13

def suitFromCard(card):
    return card // 13

def cardFromName(s):
    if len(s) < 2 or len(s) > 3:
        return -1
    pips, suit = s[:-1], s[-1]
    # print(f"pips {pips}")
    # print(f"suit {suit}")        
    if suit == "S" or suit == "s":
        suit = 0
    elif suit == "D" or suit == "d":
        suit = 1
    elif suit == "H" or suit == "h":
        suit = 2
    elif suit == "C" or suit == "c":
        suit = 3
    else:
        return -1
    
    if pips == "A" or pips == "a":
        pips = 0
    elif pips == "J" or pips == "j":
        pips = 10
    elif pips == "Q" or pips == "q":
        pips = 11
    elif pips == "K" or pips == "k":
        pips = 12
    else:
        pips = int(pips) - 1

    if (pips < 0 or pips > 12):
        return -1
    result = suit * 13 + pips    
    # print_card(result)
    return result
        


#fgcolor(color.RED)
#print("H", end="")
#fgcolor(color.BLACK)
#print("E", end="")
#fgcolor(color.RED)
#print("L", end="")
#fgcolor(color.BLACK)
#print("L", end="")
#fgcolor(color.RED)
#print("O", end="")
    



# run main test stub if this file is directly loaded    
if __name__ == '__main__':
    main()
    
