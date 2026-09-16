from board import Board

class User_Interface:
    def __init__(self, i_Board: Board):
        self.myBoard = i_Board
        self.rows = self.myBoard.getRows()
        self.cols = self.myBoard.getCols()
        self.board = [['X' for _ in range(self.cols)] for _ in range(self.rows)]

    def print_board(self,loss = False):
        print("   Remaining Flags:", self.myBoard.getNumRemainingFlags())
        print("   A B C D E F G H I J\n  ",end="")
        print(" -" * (self.rows+1))
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