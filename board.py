import random
class Board:


    def __init__(self, rows: int = 10, cols: int = 10, numMinesInput = -1):
        """creates the board with member variables rows, cols, numMines, gameState, remainingFlags, and a 2D board itself"""
        self.__rows = rows
        self.__cols = cols
        self.__numMines = numMinesInput #must be user supplied from [10, 20], if not set as -1

        """
        Board Cell State Definitions:
        0 = Unchecked and no mine
        1 = Flag (typically a false flag)
        2 = Checked and no mine
        3 = Unchecked mine
        4 = Correctly flagged mine
        """
        self.__board = [[0] * self.__rows] * self.__cols #populate board with 0's
        self.__gameState = 0 #0 is neither win or lose, -1 is lose, 1 is win
        self.__remainingFlags = numMinesInput

    def populateBoard(self, clickedCellRow, clickedCellCol):
        """adds a user specified number of mines to the board, to every space other than first click"""
        #[row][column]
        for i in range(self.getNumMines()):
            rowMine = random.randint(0, self.getRows()-1)
            colMine = random.randint(0, self.getCols()-1)
            if((rowMine == clickedCellRow and colMine == clickedCellCol) or self.getCellState(clickedCellRow, clickedCellCol) == 3):
                i = i - 1
            else:
                self.__board[rowMine][colMine] = 3

    def setState(self, clickedCellRow, clickedCelCol, isFlagging = False): # should be t/f for flagging
        """updates the states of the cells, checking if user input is flag or no flag.
        if not flagging and a 0 state cell: if cell has no bomb neighbors clear all neighbors"""
        if(isFlagging): #if right clicking, handle removing flags on 1 & 4, add flags on 3 and 0, ignore 2's
            if(self.getCellState(clickedCellRow, clickedCelCol) == 3):
                self.__board[clickedCellRow][clickedCelCol] = 4
                self.__remainingFlags -= 1
            elif(self.getCellState(clickedCellRow, clickedCelCol) == 4):
                self.__board[clickedCellRow][clickedCelCol] = 3
                self.__remainingFlags += 1
            elif(self.getCellState(clickedCellRow, clickedCelCol) == 1):
                self.__board[clickedCellRow][clickedCelCol] = 0
                self.__remainingFlags += 1
            elif(self.getCellState(clickedCellRow, clickedCelCol) == 0):
                self.__board[clickedCellRow][clickedCelCol] = 1
                self.__remainingFlags -= 1
        else: #if left clicking, only handle clicking on 0 or 3, ignore clicks on 1 2 4
            if(self.getCellState(clickedCellRow, clickedCelCol) == 3):
                self.__gameState = -1
            elif(self.getCellState(clickedCellRow, clickedCelCol) == 0):
                self.__board[clickedCellRow][clickedCelCol] = 2
                b = self.numBombNeighbors(clickedCellRow, clickedCelCol)
                if(b == 0):
                    #CLEAR ALL NEIGHBORS UNLESS FALSE FLAG AND CONTINUE FOR EACH 0 ADJACENT
                    for i in range(self.getRows()):
                        for j in range(self.getCols()):
                            self.setState(i, j)

    def hasWon(self):
        """returns the gamestates, if -1 player has lost, if 0 the game is not over, if 1 the player has won"""
        if(self.__gameState == -1):
            return -1

        for i in range(self.getRows):
            for j in range(self.getCols):
                if(self.getCellState(i, j) == 0 or self.getCellState(i, j) == 1):
                    self.__gameState = 0
                    return 0
        
        self.__gameState = 1
        return 1

    def __checkAdjCells(self, row, col):
        """creates and returns a map of the cell states for each adjacent cell of a given cell"""
        adjCellMap = [0, 0, 0,
                    0, -2, 0,
                    0, 0, 0] #-2 == self cell, -1 refers to not on grid (used for when cell is adjacent to walls)
        if(row == 0):
            adjCellMap[0] = -1
            adjCellMap[1] = -1
            adjCellMap[2] = -1
        elif(row == self.getRows()-1):
            adjCellMap[6] = -1
            adjCellMap[7] = -1
            adjCellMap[8] = -1
        if(col == 0):
            adjCellMap[0] = -1
            adjCellMap[3] = -1
            adjCellMap[6] = -1
        elif(col == self.getCols()-1):
            adjCellMap[2] = -1
            adjCellMap[5] = -1
            adjCellMap[8] = -1


        #0 = row-1, col-1
        #1 = row-1
        #2 = row-1, col+1
        for i in range(9):
            if(adjCellMap[i] == 0):
                adjCellMap[i] = self.getCellState(row+((i//3)-1), col+((i%3)-1))

        return adjCellMap
                
    def numBombNeighbors(self, row, col):
        """Returns the number of bombs adjacent to a cell, given a cell location"""
        adjCellList = self.__checkAdjCells(row, col)
        numBombsAdj = 0
        for elem in adjCellList:
            if(elem == 3):
                numBombsAdj += 1
        return numBombsAdj

    def getRows(self):
        """return the number of rows"""
        return self.__rows
    def getCols(self):
        """return the number of columns"""
        return self.__cols
    def getCellState(self, row, col):
        """return the state of a cell

        SHOULD PRIMARILY BE USED OUTSIDE OF CLASS ONLY WHEN GAMESTATE = -1 or 1 to display false flags or remaining mine locations, otherwise use numBombNeighbors to display a number on a cell

        0 = Unchecked and no mine
        1 = Flag (typically a false flag)
        2 = Checked and no mine
        3 = Unchecked mine
        4 = Correctly flagged mine
        """
        return self.__board[row][col]
    def getNumRemainingFlags(self):
        """return the number of remaining flags (can go negative for false flags)"""
        return self.__remainingFlags
    def getNumMines(self):
        return self.__numMines
