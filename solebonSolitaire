import color
import cards2
import pickle
import sys
import random
import time
import os

class RussianRevolver:


    def __init__(self):
        '''
        Initialization of a RussianRevolver "game". 
        '''
        self.piles = [ [], [], [], [], [], [] ]
        self.shown = [ [], [], [], [], [], [] ]
        self.foundation = [ [], [], [], [] ]
        self.deck = []
        self.shuffles = 6
        self.moves = 0
        self.history = []


    def newDeck(self):
        '''
        Creates a brand new deck.
        '''
        self.deck = cards2.fresh_deck()
        cards2.shuffle(self.deck)


    def shuf(self):
        '''
        Shuffles a deck, without placing the cards in piles.                                                                                                                     
        '''
        self.deck = []
        for pile in self.piles:
            self.deck += pile
        cards2.shuffle(self.deck)


    def clearPiles(self):
        '''
        Clears the piles and shown status lists.
        '''
        self.piles = [ [], [], [], [], [], [] ]
        self.shown = [ [], [], [], [], [], [] ]


    def deal(self):
        '''
        Takes a deck and deals the cards. Two cards are dealt face up in each
        column, then the remaining cards are split among the other columns.                                                                                                                                                                                                                                                                  
        Each of the last five columns has three face down cards at the top.
        If there are not enouch cards in these columns, the last card of each 
        column is "flipped over" and shown.
        '''
        self.clearPiles()
        num_cards = len(self.deck)
        self.piles[0] = [self.deck.pop(), self.deck.pop()]
        self.shown[0] = [True, True]
        next = 1
        row = 1
        while self.deck:
            show = (row > 3)
            self.piles[next].append(self.deck.pop())
            self.shown[next].append(show)
            next = next + 1
            if next == 6:
                next = 1
                row += 1
        if num_cards < 22:  # Make sure the last card in every pile is flipped
            for i in range(1, 6):
                if self.piles[i]: # Except for empty piles
                    self.shown[i][-1] = True


    def printBoard(self, print_status = True):
        '''
        This displays the piles and foundations, as well as the number of moves
        used and shuffles left. This should be called after each move.
        '''
        if not print_status:
            return
        color.bgcolor(color.GREEN)
        print("\n", flush = True)
        for i in self.foundation:
            if i:
                cards2.print_card(i[-1], True)
            else:
                cards2.print_card(-1)
        print (f'   shuffles: {self.shuffles}, moves: {self.moves}')
        print('\n')
        lens = [len(pile) for pile in self.piles]
        row_count = max(lens)
        for row in range(0, row_count):
            for col in range(0, 6):
                if len(self.piles[col]) > row:
                    cards2.print_card(self.piles[col][row], self.shown[col][row])
                else:
                    cards2.print_blank()
            print('')
        print('')


    def find(self, card):
        '''
        Looks for a card and returns column and row if it is visible.                                    
        Returns False if not visible.
        '''
        for i in range(0, 6):
            if card in self.piles[i]:
                col = i
                row = self.piles[i].index(card) # rows are from 0
                show = self.shown[i][row]
                if show:
                    return col, row
                else:
                    return False
    
            
    def moveNonKing(self, card, to_col, from_col, row):
        '''
        Used to move cards that are not kings.
        '''
        if self.isValid(card, to_col, from_col):
            self.moveStack(to_col, from_col, row)


    def moveKing(self, to_col, from_col, row):
        '''
        Used to move kings to empty columns.
        '''
        if not self.piles[to_col]:
            self.moveStack(to_col, from_col, row)
                

    def isValid(self, card, to_col, from_col):
        '''
        Checks if the card can be moved to the selected column. Only necessary
        for cards that are not kings, because kings can only move to an empty
        column.
        '''
        if from_col == to_col:
            return False
        elif self.piles[to_col]:
            return self.piles[to_col][-1] == cards2.nextCard(card)       
    

    def moveStack(self, to_col, from_col, row):
        '''
        Transfers a card and all the cards below it to another pile.
        '''
        self.piles[to_col] = self.piles[to_col] + self.piles[from_col][row:]
        self.shown[to_col] = self.shown[to_col] + self.shown[from_col][row:]
        del self.piles[from_col][row:]
        del self.shown[from_col][row:]
        if self.shown[from_col]:
            self.shown[from_col][-1] = True
        self.moves += 1


    def checkFoundation(self, card):
        '''
        If the card is an ace, checks to see if any foundations are empty. If
        the card is not an ace, checks to see if the card of the same suit and
        one lower pips is at the top of any foundations. Returns the foundation
        that can be moved onto, or None if no foundation piles can be moved onto.
        '''
        if cards2.isAce(card):
            for found in self.foundation:
                if not found:
                    return found
        for found in self.foundation:
            if cards2.prevCard(card) in found:
                return found
        return None
    

    def moveToFoundation(self, card, from_col, row, found):
        '''
        Moves a card to a specified foundation pile.
        '''
        if found == None:
            return
        found.append(card)
        del self.piles[from_col][row]
        del self.shown[from_col][row]
        if self.shown[from_col]:
            self.shown[from_col][-1] = True
        self.moves += 1
        addToHistory(self)


    def autoFoundation(self):
        '''
        If prompted, this makes all eligible moves to the foundation. Repeats
        until no more cards can be moved.
        '''
        foundation_moves = True
        while foundation_moves:
            last_cards = [pile[-1] for pile in self.piles if pile]
            foundation_moves = 0
            for card in last_cards:
                found = self.checkFoundation(card)
                if found != None:
                    foundation_moves += 1
                from_col, row = self.find(card)
                self.moveToFoundation(card, from_col, row, found)


    def move(self, card):
        '''
        Moves the selected card to the foundation if possible. If not possible,
        prompts for a destination column and redirects to moveNonKing() or
        moveKing().
        '''
        result = self.find(card)
        if not result:
            print ("Card not found")
            return
        from_col, row = result
        found = self.checkFoundation(card)
        if card == self.piles[from_col][-1] and found != None:
            self.moveToFoundation(card, from_col, row, found)
            return
        column = input('Column (1-6)? ')
        columns = ['1', '2', '3', '4' , '5', '6']
        if column.strip() not in columns: 
            print ("Not a valid column")
            return
        to_col = int(column) - 1
        if cards2.isKing(card):
            self.moveKing(to_col, from_col, row)
            addToHistory(self)
            return
        else:
            self.moveNonKing(card, to_col, from_col, row)
            addToHistory(self)
            return


    def movePossible(self, card, to_col):
        '''
        A function that mirrors move() in many ways. Instead of actually moving
        the card to the destination column, it returns True if it is possible
        to move the card and False if it is not possible. Used only in the
        hint() function.
        '''
        result = self.find(card)
        if not result:
            return False
        from_col = result[0]
        found = self.checkFoundation(card)
        if card == self.piles[from_col][-1] and found != None:
            return 'Foundation'
        if cards2.isKing(card) and not self.piles[to_col]:
            return to_col + 1
        elif self.isValid(card, to_col, from_col):
            return to_col + 1
        return False


    def hint(self):
        '''
        Provides the user with a possible move.
        '''
        moves = []
        pips = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suit = ['♠', '♦', '♥', '♣']
        for to_col in range(0, 6):
            for card in range(0, 52):
                dest = self.movePossible(card, to_col)
                if dest:
                    moves.append((card, dest))
        if moves:
            card, dest = moves[random.randrange(0, len(moves))]
            hint_pips = pips[cards2.pipsFromCard(card)]
            hint_suit = suit[cards2.suitFromCard(card)]
            if dest == 'Foundation':
                print_slowly(f'{hint_suit + hint_pips} to foundation is a possible move.')
            else:
                print_slowly(f'{hint_suit + hint_pips} to column {dest} is a possible move.')
            return True
        else:
            print_slowly("No moves available. Type 'shuf' to shuffle or 'end' to end the game.")
            return False


commands = ['shuf', 'load', 'save', 'end', 'undo', 'help', 'cheat', 'auto', 'hint']

def main():
    if not os.path.exists('./savedGames'):
        os.makedirs('./savedGames')
    game = RussianRevolver()
    print_slowly('Hello! Type "n" to start a new game, or "l" to load a previous game.')
    choice = input()
    while choice != 'n' and choice != 'l':
        print_slowly('Please type "n" or "l".')
        choice = input()
    if choice == 'l':
        loaded = load(game)
    if choice == 'n' or not loaded:
        game.newDeck()
        game.deal()
        addToHistory(game)
    print_slowly('Reminder: the possible commands are "shuf", "save", "end", "undo",', ending = ' ')
    print_slowly('"cheat", "auto", "hint", and "help".')
    time.sleep(1)
    print_slowly('Type "help" at any time to see the list of commands and their explanations.')
    time.sleep(1)
    print_slowly('Have fun!')
    time.sleep(1)
    game.printBoard()
    print('')
    takeCommand(game)


def print_slowly(message, ending = '\n'):
    '''
    Special printing style for this project.
    '''
    for char in message[0:-1]:
        print(char, end = '', flush = True)       
        time.sleep(0.000000001)
    print(message[-1], end = ending)


def takeCommand(game):
    '''
    This function distinguishes between commands and takes the appropriate action.
    '''
    for line in sys.stdin:
        print_status = True
        line = line.strip().lower()
        if line not in commands:
            if isCard(line):
                card = cards2.cardFromName(line)
                game.move(card)
        elif line == 'shuf':
            if game.shuffles:
                game.shuf()
                game.deal()
                game.shuffles -= 1
                game.moves += 1
                addToHistory(game)
            else:
                print_slowly('No shuffles left!')
        elif line == 'load':
            load(game)
        elif line == 'save':
            save(game)
            return
        elif line == 'end':
            return
        elif line == 'undo':
            undo(game)
        elif line == 'help':
            help()
        elif line == 'cheat':
            game.shuffles += 6
        elif line == 'auto':
            game.autoFoundation()
        elif line == 'hint':
            result = game.hint()
            time.sleep(1)
            if result:
                print_slowly('Go ahead and make that move, or any other move you see.')
            print_status = False
        game.printBoard(print_status)   
        if not any(game.piles):
            message = f'Congratulations! You won in {game.moves} moves!'
            print_slowly(message)
            return


def isCard(text):
    '''
    Returns True if the entered text is a valid card.
    '''
    pips = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    suit = ['c', 'd', 'h', 's']
    try:
        text1 = text[:-1].lower()
        text2 = text[-1].lower()
        return  (text1 in pips) and (text2 in suit)
    except:
        return False


def addToHistory(game):
    '''
    Adds all of the attributes of the game to a list.
    Appends this list to an ordered history of all previous game states.
    '''
    gameList = [game.piles, game.shown, game.foundation, game.deck, game.shuffles, game.moves]   
    game.history.append(pickle.dumps(gameList))


def undo(game):
    '''
    Undoes the last move. After this is called, the previous game
    board is printed.
    '''
    if len(game.history) > 1:
        game.history.pop()
        gameList = pickle.loads(game.history[-1])
        game.piles, game.shown, game.foundation, game.deck, game.shuffles, game.moves = gameList
    return game


def load(game):
    '''
    Loads a previously saved game.
    If no game is found with the provided name, starts a new game.
    '''
    print_slowly('What is the name of the game you would like to load?')
    selection = input()
    prevGames = []
    for file in os.listdir('./savedGames'):
        prevGames.append(file)
    if selection not in prevGames:
        print_slowly("There are no previous games with that name. I'll start a new game for you!")
        return False
    path = f'./savedGames/{selection}'
    with open(path, 'rb') as prevGame:
        game.history = pickle.load(prevGame)
        gameList = pickle.loads(game.history[-1])
        game.piles, game.shown, game.foundation, game.deck, game.shuffles, game.moves = gameList
    return True


def save(game):
    '''
    Saves the current game in a separate directory.
    '''
    print_slowly('What would you like to name this game? ')
    saveName = str(input())
    path = f'./savedGames/{saveName}'
    with open(path, 'wb') as saveFile:
        pickle.dump(game.history, saveFile)


def help():
    '''
    Gives the user a useful help menu.
    '''
    print_slowly("The 'shuf' command shuffles and redeals the cards. It could be useful")
    print_slowly("if you ever run out of moves! Careful though; you can only shuffle 6 times!")
    time.sleep(1)
    print_slowly("The 'load' command stops your game in its place and loads a previous game.")
    time.sleep(1)
    print_slowly("The 'save' command allows you to save your game with a name of your choice.")
    print_slowly("That way, you can take a break and pick your game back up later!")
    time.sleep(1)
    print_slowly("The 'end' command ends your game, without saving it.")
    time.sleep(1)
    print_slowly("The 'undo' command reverses your previous move, and brings your move counter")
    print_slowly("down by 1. You can use this command any number of times.")
    time.sleep(1)
    print_slowly("The 'cheat' command increases your available shuffles by 6. Try not to use")
    print_slowly("that one too much if you want a challenge!")
    time.sleep(1)
    print_slowly("The 'auto' command will automatically make all possible foundation moves.")
    print_slowly("That could save you a lot of time at the end of the game!")
    time.sleep(1)
    print_slowly("The 'hint' command gives you a possible move, if you find yourself really stuck!")


if __name__ == '__main__':
    main()
