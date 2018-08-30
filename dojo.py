# 10 by 10

import numpy as np


class Board():

    def __init__(self):
        self.board = np.zeros(shape=(10,10))

        self.ships = {'carrier': np.ones(5),
                'battleship': np.ones(4),
                'cruser': np.ones(3),
                'submarine': np.ones(3),
                'destroyer': np.ones(2)
                }

        self.letters = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
                        'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
                        'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
                       }

    def place_ship(self, name, orientation, num, letter):
            num = int(num)
            lett = self.letters[letter]
            ship = np.pad(self.ships[name], (num-1, (10-(num-1)-len(self.ships[name]))), 'constant' )

            if orientation == 'hor':
                new_row = self.board[lett-1,:] + ship

                if new_row.flatten()[new_row.argmax()] == 1:
                    self.board[lett-1,:] = self.board[lett-1,:] + ship
                else:
                    raise ValueError('You are trying to place a ship on top of another ship.')

            elif orientation == 'ver':
                new_col = self.board[:, lett-1] + ship
                if new_col.flatten()[new_col.argmax()] == 1:
                    self.board[:,lett-1] = self.board[:,lett-1] + ship
                else:
                    raise ValueError('You are trying to place a ship on top of another ship.')

            else:
                raise ValueError('This paramater must be on of "hor" or "ver"')


    def hit(self, num, letter):
        if self.board[num-1,self.letters[letter]-1] > 0:
            return True
        else:
            return False

    def show_board(self):
        print(self.board)

class Game(Board):
    def __init__(self, name1, name2):
        self.player1 = {name:name1, points:0}

    # def win(self,player):
