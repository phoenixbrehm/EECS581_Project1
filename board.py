#board.py
"""
Author: Phoenix Brehm and Carson Schraad, Created 9/10/26
Last updated: 9/15/26 - by Phoenix Brehm
Code is authored by Phoenix Brehm, with Carson Schraad creating the function prototype alongside member variables rows and cols for __init__ with Claude as a co-author (used the ai to assist in pushing the change made to the github) see AI disclosure document on usage for this file
Board Class
The goal of the board class is to implement functions that manage the board
Functions implemented are:
    init which takes in a user specified number of mines, returns none
    populateBoard takes in a row and column, returns none
    setState takes in a row column and isFlagging variable, returns none
    hasWon takes in no variables, returns an int -1, 0, 1
    __checkAdjCells takes in a row and col, returns a list of ints
    numBombNeighbors takes in a row and col, returns an int
    getRows takes in no varaibles, returns int
    getCols takes in no varaibles, returns int
    getCellState takes in a row and col, returns int
    getNumRemainingFlags takes in no varaibles, returns int
    getNumMines takes in no varaibles, returns int
"""
import random
class Board:


    def __init__(self, numMinesInput: int = -1, rows: int = 10, cols: int = 10):
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
        self.__board = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)] #populate board which is a 2d array with 0's
        self.__gameState = 0 #0 is neither win or lose, -1 is lose, 1 is win
        self.__remainingFlags = numMinesInput #remaining flags is number of mines - flags placed (can go negative for false flags)

    def populateBoard(self, clickedCellRow: int, clickedCellCol: int):
        """adds a user specified number of mines to the board, to every space other than first click"""
        #[row][column]
        minesplaced = 0
        while(minesplaced < self.getNumMines()):
            rowMine = random.randint(0, self.getRows()-1)
            colMine = random.randint(0, self.getCols()-1)
            if((rowMine == clickedCellRow and colMine == clickedCellCol) or self.getCellState(rowMine, colMine) == 3): #if we generate on clicked cell location or where a mine already exists
                continue #try again
            else:
                self.__board[rowMine][colMine] = 3
                minesplaced += 1

    def setState(self, clickedCellRow: int, clickedCelCol: int, isFlagging: bool = False): # should be t/f for flagging
        """updates the states of the cells, checking if user input is flag or no flag.
        if not flagging and a 0 state cell: if cell has no bomb neighbors clear all neighbors"""
        if(isFlagging): #if right clicking, handle removing flags on 1 & 4, add flags on 3 and 0, ignore 2's
            if(self.getCellState(clickedCellRow, clickedCelCol) == 3): #if right click a bomb
                self.__board[clickedCellRow][clickedCelCol] = 4 #place a flag
                self.__remainingFlags -= 1 #decrease remaining flags
            elif(self.getCellState(clickedCellRow, clickedCelCol) == 4): #if right click a flagged bomb
                self.__board[clickedCellRow][clickedCelCol] = 3 #remove flag
                self.__remainingFlags += 1 #increase remaining flags
            elif(self.getCellState(clickedCellRow, clickedCelCol) == 1):
                self.__board[clickedCellRow][clickedCelCol] = 0
                self.__remainingFlags += 1
            elif(self.getCellState(clickedCellRow, clickedCelCol) == 0): #if right click on normal unchecked cell
                self.__board[clickedCellRow][clickedCelCol] = 1 #place false flag
                self.__remainingFlags -= 1
        else: #if left clicking, only handle clicking on 0 or 3, ignore clicks on 1 2 4
            if(self.getCellState(clickedCellRow, clickedCelCol) == 3): #if left click bomb
                self.__gameState = -1 #game over
            elif(self.getCellState(clickedCellRow, clickedCelCol) == 0): #if left click unchecked cell
                self.__board[clickedCellRow][clickedCelCol] = 2 #set it to 2
                b = self.numBombNeighbors(clickedCellRow, clickedCelCol) #check how many bomb neighbors it has
                if(b == 0):
                    #CLEAR ALL NEIGHBORS UNLESS FALSE FLAG AND CONTINUE FOR EACH 0 ADJACENT
                    #clear row-1 col-1
                    #clear row-1 col
                    for i in range(9):
                        checkRow = clickedCellRow+((i//3)-1)
                        checkCol = clickedCelCol+((i%3)-1)
                        if checkRow < 0 or checkCol < 0 or checkRow > self.getRows()-1 or checkCol > self.getCols()-1: #index checking
                            continue
                        else:
                            self.setState(checkRow, checkCol) #recursively clear all neighbors as long as caller is has 0 bombs nearby
                            #print(self) debug line

    def hasWon(self):
        """returns the gamestates, if -1 player has lost, if 0 the game is not over, if 1 the player has won"""
        if(self.__gameState == -1):
            return -1

        for i in range(self.getRows()):
            for j in range(self.getCols()):
                if(self.getCellState(i, j) == 0 or self.getCellState(i, j) == 1): #if any 0's or 1's exist on the board the player has not won
                    self.__gameState = 0
                    return 0
        
        self.__gameState = 1
        return 1

    def __checkAdjCells(self, row: int, col: int):
        """creates and returns a map of the cell states for each adjacent cell of a given cell"""
        adjCellMap = [0, 0, 0,
                    0, -2, 0,
                    0, 0, 0] #-2 == self cell, -1 refers to not on grid (used for when cell is adjacent to walls)

        #manually setting each wall to -1
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
            if(adjCellMap[i] == 0): #checks all non edge adjacent cells
                adjCellMap[i] = self.getCellState(row+((i//3)-1), col+((i%3)-1)) #get the state of cells in each direction that isn't a wall

        return adjCellMap
                
    def numBombNeighbors(self, row: int, col: int):
        """Returns the number of bombs adjacent to a cell, given a cell location"""
        adjCellList = self.__checkAdjCells(row, col) #get the list of status of adjacent cells
        numBombsAdj = 0
        for elem in adjCellList:
            if(elem == 3 or elem == 4): #for each bomb in the list, increment the number of bombs adjacent by 1
                numBombsAdj += 1
        return numBombsAdj

    def getRows(self):
        """return the number of rows"""
        return self.__rows
    def getCols(self):
        """return the number of columns"""
        return self.__cols
    def getCellState(self, row: int, col: int):
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
        """return the number of mines the user provided"""
        return self.__numMines
