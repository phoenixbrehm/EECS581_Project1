from board import Board
import random
from input_handler import get_input

# Board __init__ test
test = Board(10)
print(vars(test))

# populateBoard() tests
# - Test 1: Regular Run (No Additions / Alterations)
# - Test 2: Run that forces the last mine to be on the clicked cell row and column (which also tests how the other condition will run as well)

print("\n-------- populateBoard() --------")
print("Test 1:")
test.populateBoard(1, 1)
print(test._Board__board)
# Result as of 9/12/26 - Working as intended


print("Test 2: ")
test = Board(11) #resets board state

def populateBoard_t2(self, clickedCellRow: int, clickedCellCol: int):
        """adds a user specified number of mines to the board, to every space other than first click"""
        #[row][column]
        for i in range(self.getNumMines()):
            rowMine = random.randint(0, self.getRows()-1)
            colMine = random.randint(0, self.getCols()-1)

            #ALTERATION BEGIN, FORCES THE TEST TO OCCUR AT THE END
            if i == self.getNumMines() - 1:
                rowMine = clickedCellRow
                colMine = clickedCellCol

            if((rowMine == clickedCellRow and colMine == clickedCellCol) or self.getCellState(clickedCellRow, clickedCellCol) == 3):
                i = i - 1
            else:
                self._Board__board[rowMine][colMine] = 3

func_buffer = test.populateBoard
Board.populateBoard = populateBoard_t2

test.populateBoard(1, 1)
print(test._Board__board)

Board.populateBoard = func_buffer
func_buffer = None

# setState() tests
# - Tests 1: Flagging Checks

# initial setting up of clickedCellRows to ensure for flagging check
test = Board(10)
test.populateBoard(1, 1)
test._Board__board[0][0] = 3
test._Board__board[0][1] = 4
test._Board__board[0][2] = 1
test._Board__board[0][3] = 0

print("\n-------- setState() --------")
print("Tests 1: ")

test.setState(0, 0, True)
print(test.getCellState(0, 0))
print("# of Remaining Flags: " + str(test.getNumRemainingFlags()) + "\n")

test.setState(0, 1, True)
print(test.getCellState(0, 1))
print("# of Remaining Flags: " + str(test.getNumRemainingFlags()) + "\n")

test.setState(0, 2, True)
print(test.getCellState(0, 2))
print("# of Remaining Flags: " + str(test.getNumRemainingFlags()) + "\n")

test.setState(0, 3, True)
print(test.getCellState(0, 3))
print("# of Remaining Flags: " + str(test.getNumRemainingFlags()) + "\n")

print("Tests 2: ")
test.setState(0,1, False)
print("Game state: " + str(test.hasWon()))

test._Board__gameState = 0
print(test._Board__board) 
r = int(input("Please provide row: ")) # manual test case to determine if neighbors are properly being uncovered
c = int(input("Please provide col: "))
test.setState(r, c, False)
print(test._Board__board)

print("\n-------- __checkAdjCells() --------")

#__checkAdjCells() tests
#checking cell states of out of bounds neighbors
#out of bounds neighbors should have state -1

print("Tests 1: bottom row neighbor states") #test case to check neighbor states of all bottom row cells, neighbors below should have state -1
i = 0
for i in range(10):
    print("cell neighbor states, col ", str(i), ": ", test._Board__checkAdjCells(9, i)) 

print("\nTests 2: top row neighbor states") #test case to check neighbor states of all top row cells, neighbors above should have state -1
i = 0
for i in range(10):
    print("cell neighbor states, col ", str(i), ": ", test._Board__checkAdjCells(0, i))

print("\nTests 3: left column neighbor states") #test case to check neighbor states for all left column cells, neighbors to the left should have state -1
i = 0
for i in range(10):
     print("cell neighbor states, row ", str(i), ": ", test._Board__checkAdjCells(i, 0))

print("\nTests 4: right column neighbor states") #test case to check neighbor states for all right column cells, neighbors to the right should have state -1
i = 0
for i in range(10):
     print("cell neighbor states, row ", str(i), ": ", test._Board__checkAdjCells(i, 9))

print("\n-------- get_input() --------")

#get_input() tests
#check for invalid inputs

for i in range(6):
    print("\nTest ", str(i+1), ":")
    get_input() #manual test case to check handling of invalid inputs
