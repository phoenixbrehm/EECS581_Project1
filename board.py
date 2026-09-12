import random
class Board:


    def __init__(self, rows: int = 10, cols: int = 10, numMines = -1):
        self.rows = rows
        self.cols = cols
        self.numMines = numMines #must be user supplied from [10, 20], if not set as -1

        """
        Board Cell State Definitions:
        0 = Unchecked and no mine
        1 = Flag (typically a false flag)
        2 = Checked and no mine
        3 = Unchecked mine
        4 = Correctly flagged mine
        """
        self.board = [[0] * self.rows] * self.cols #populate board with 0's
        self.gameState = 0 #0 is neither win or lose, -1 is lose, 1 is win

    def populateBoard(self, clickedCellRow, clickedCellCol):
        #row is each set of lists
        for i in range(self.numMines):
            rowMine = random.randint(0, self.rows-1)
            colMine = random.randint(0, self.cols-1)
            if(rowMine == clickedCellRow and colMine == clickedCellCol and self.board[rowMine][colMine] == 3):
                i = i - 1
            else:
                self.board[rowMine][colMine] = 3

    def setState(self, clickedCellRow, clickedCelCol, isFlagging = False): # should be t/f
        if(isFlagging): #if right clicking, handle removing flags on 1 & 4, add flags on 3 and 0, ignore 2's
            if(self.board[clickedCellRow][clickedCelCol] == 3):
                self.board[clickedCellRow][clickedCelCol] = 4
            elif(self.board[clickedCellRow][clickedCelCol] == 1):
                self.board[clickedCellRow][clickedCelCol] = 0
            elif(self.board[clickedCellRow][clickedCelCol] == 4):
                self.board[clickedCellRow][clickedCelCol] = 3
            elif(self.board[clickedCellRow][clickedCelCol] == 0):
                self.board[clickedCellRow][clickedCelCol] = 1
        else: #if left clicking, only handle clicking on 0 or 3, ignore clicks on 1 2 4
            if(self.board[clickedCellRow][clickedCelCol] == 3):
                self.gameState = -1
            elif(self.board[clickedCellRow][clickedCelCol] == 0):
                pass

    def hasWon(self):
        if(self.gameState == -1):
            return -1

        for i in range(self.rows):
            for j in range(self.cols):
                if(self.board[i][j] == 0 or self.board[i][j] == 1):
                    self.gameState = 0
                    return 0
        
        self.gameState = 1
        return 1

    