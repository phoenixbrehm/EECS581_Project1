import random
class Board:


    def __init__(self, rows: int = 10, cols: int = 10, numMines = -1):
        self.__rows = rows
        self.__cols = cols
        self.__numMines = numMines #must be user supplied from [10, 20], if not set as -1

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
        self.__remainingFlags = numMines

    def populateBoard(self, clickedCellRow, clickedCellCol):
        #row is each set of lists
        for i in range(self.__numMines):
            rowMine = random.randint(0, self.getRows()-1)
            colMine = random.randint(0, self.getCols()-1)
            if(rowMine == clickedCellRow and colMine == clickedCellCol and self.__board[rowMine][colMine] == 3):
                i = i - 1
            else:
                self.__board[rowMine][colMine] = 3

    def setState(self, clickedCellRow, clickedCelCol, isFlagging = False): # should be t/f
        if(isFlagging): #if right clicking, handle removing flags on 1 & 4, add flags on 3 and 0, ignore 2's
            if(self.__board[clickedCellRow][clickedCelCol] == 3):
                self.__board[clickedCellRow][clickedCelCol] = 4
                self.__remainingFlags -= 1
            elif(self.__board[clickedCellRow][clickedCelCol] == 4):
                self.__board[clickedCellRow][clickedCelCol] = 3
                self.__remainingFlags += 1
            elif(self.__board[clickedCellRow][clickedCelCol] == 1):
                self.__board[clickedCellRow][clickedCelCol] = 0
                self.__remainingFlags += 1
            elif(self.__board[clickedCellRow][clickedCelCol] == 0):
                self.__board[clickedCellRow][clickedCelCol] = 1
                self.__remainingFlags -= 1
        else: #if left clicking, only handle clicking on 0 or 3, ignore clicks on 1 2 4
            if(self.__board[clickedCellRow][clickedCelCol] == 3):
                self.__gameState = -1
            elif(self.__board[clickedCellRow][clickedCelCol] == 0):
                self.__board[clickedCellRow][clickedCelCol] = 2
                adjCells = self.checkAdjCells(clickedCellRow, clickedCelCol)
                #if all adjCells

    def hasWon(self):
        if(self.__gameState == -1):
            return -1

        for i in range(self.__rows):
            for j in range(self.__cols):
                if(self.__board[i][j] == 0 or self.__board[i][j] == 1):
                    self.__gameState = 0
                    return 0
        
        self.__gameState = 1
        return 1

    def checkAdjCells(self, row, col):
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
                
    def numBombNeighbors(self, adjCellList):
        numBombsAdj = 0
        for elem in adjCellList:
            if(elem == 3):
                numBombsAdj += 1
        return numBombsAdj

    def getRows(self):
        return self.__rows
    def getCols(self):
        return self.__cols
    def getCellState(self, row, col):
        return self.__board[row][col]
    def getNumRemainingFlags(self):
        return self.__remainingFlags