#user_interface.py
"""
Author: Collin Tullis created 9/13/26
Last updated: 9/20/26 - by Collin Tullis
user_interface.py handles outputing the board state to the terminal for the user to interact with
Functions implemented are:
    __init__, which takes in a Board and extracts relevant information
    print_board, which takes in if a loss has occured and returns a visualization of the current board state
    main which takes in no input and returns none
"""

from board import Board

class User_Interface:
    def __init__(self, i_Board: Board):
        self.myBoard = i_Board 
        self.rows = self.myBoard.getRows()
        self.cols = self.myBoard.getCols()
        self.board = [['X' for _ in range(self.cols)] for _ in range(self.rows)] #creates a correctly sized board

    def print_board(self,loss = False):
        print("   Remaining Flags:", self.myBoard.getNumRemainingFlags())
        print("   A B C D E F G H I J\n  ",end="")
        print(" -" * (self.rows+1))
        """
        Loop through each spot on the Board
        If the game is still going, do not show where the mines are
        If the game is over, show where the mines are
        X for unchecked spot
        F for a flag
        M for a mine (only if the game is finished)
        A number for a cleared spot with a mine(s) nearby
        An empty space for a checked space with no nearby mines
        """
        for row in range(self.rows):
            row_string = str(row+1)
            if(row != 9):
                row_string += " "
            row_string += "|"
            for col in range(self.cols):
                state = self.myBoard.getCellState(row, col)
                if(not loss):
                    if state == 0 or state == 3: #unchecked spot
                        row_string += "X "
                    elif state == 1 or state == 4: #flagged spot
                        row_string += "F "
                    elif state == 2: # checked spot with no mine
                        if(self.myBoard.numBombNeighbors(row, col) != 0):
                            row_string += (str(self.myBoard.numBombNeighbors(row, col)) + " ")
                        else:
                            row_string += "  "
                else:
                    if state == 0: #unchecked spot
                        row_string += "X "
                    elif state == 3:
                        row_string += "M "
                    elif state == 4: #flagged spot
                        row_string += "F "
                    elif state == 1:
                        row_string += "/ "
                    elif state == 2: # checked spot with no mine
                        if(self.myBoard.numBombNeighbors(row, col) != 0):
                            row_string += (str(self.myBoard.numBombNeighbors(row, col)) + " ")
                        else:
                            row_string += "  "
            row_string += "|"
            print(row_string)
        print("  ", end="")
        print(" -" * (self.rows+1))