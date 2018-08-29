# 10 by 10

import numpy as np


class Board():

    def __init__(self):
        self.board = np.zeros(shape=(10,10))
{}}
        self.ships = {'carrier': np.ones(shape=(1,5)),
                'battleship': np.ones(shape=(1,4)),
                'cruser': np.ones(shape=(1,3)),
                'submarine': np.ones(shape=(1,3)),
                'destroyer': np.ones(shape=(1,2))
                }

        self.letters = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
                        'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
                        'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
                       }

    def place_ship(self, name, orientation, num, letter):
        try:
            if orientation == 'hor':
                ship = np.pad(self.ships[name], (num-1, (10-(num-1)-self.ships[name].shape()[1])), 'constant', constant_values=(0, 0) )
                self.board = self.board[:,self.letters[letter]-1] + ship

            elif orientation == 'ver':
                # transpose this for vertical ships
                ship = np.pad(ships[name],(num-1,10-(num-1)-ship[name].shape()[5]))
                self.board =  self.board[:,self.letters[letter]-1] + ship

            else:
                print('Bad orientation.')

        except:
            pass



    def hit(self, num, letter):
        if self.board[num,letters[letter]] == 1:
            return True
        else:
            return False

    def show_board(self):
        print(self.board)

class Game(Board):
    def __init__(self, name1, name2):
        self.player1 = {name:name1, points:0}

    def win(self,player):
        

