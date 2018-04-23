import copy

BOARD_WIDTH = 20
BOARD_HEIGHT = 20
# y always goes first! Blame arrays.
INITIAL_CELLS = [[5,4], [5,5], [5,6]]



class Board:
    def __init__(self, width, height, initial_cells):
        # setup initial board
        self.board = []
        for y in range(0, height + 1):
            row = []
            for x in range(0, width + 1):
                row.append(0)
            self.board.append(row)
        
        # activate cells
        for coordinates in initial_cells:
            self.board[coordinates[0]][coordinates[1]] = 1
            

    def next_frame(self):  
        
        def count_live_neighbours(y, x):            
            num_alive = 0
            for neighbour_y in range(-1, 2):
                for neighbour_x in range(-1, 2):
                    if neighbour_y == 0 and neighbour_x == 0:
                        continue  
                    print(y, x, y + neighbour_y, x + neighbour_x)
                    new_y = y + neighbour_y
                    new_x = x + neighbour_x
                    if new_y < len(self.board) and new_y >= 0:
                        if new_x < len(self.board[0]) and new_x >= 0:
                            print(self.board[new_y][new_x])
                            if self.board[new_y][new_x] == 1:
                                num_alive += 1
            return num_alive

        new_board = copy.deepcopy(self.board)
        for y in range(0, len(self.board)):
            for x in range(0, len(self.board[0])):
                num_live_neighbours = count_live_neighbours(y, x)
                cell = self.board[y][x]
                if cell == 0:
                    if num_live_neighbours == 3:
                        new_board[y][x] = 1
                    else:
                        new_board[y][x] = 0
                elif cell == 1:
                    if num_live_neighbours < 2:
                        # kill
                        new_board[y][x] = 0
                    elif num_live_neighbours >= 2 and num_live_neighbours <= 3:
                        new_board[y][x] = 1
                    elif num_live_neighbours > 3:
                        # kill
                        new_board[y][x] = 0
        
        # return new board
        self.board = new_board
        


BOARD = Board(BOARD_HEIGHT, BOARD_WIDTH, INITIAL_CELLS)

def setup():
    size(BOARD_WIDTH * 10 , BOARD_HEIGHT * 10)
    frameRate(1)
    
def draw():
    pass
    
def mousePressed():
    # draw active cells
    for y in range(0, len(BOARD.board)):
        for x in range(0, len(BOARD.board[1])):
            if BOARD.board[y][x] == 1:
                fill(0)
            else:
                fill(255)
            rect(x*10, y*10, 10, 10)
                
    BOARD.next_frame()
    print('next')
    
    
    
    
    

