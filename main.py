from board import Board
from input_handler import get_input
def main():
    while(True):
        print("Welcome to Minesweeper!")
        uInput = input("Enter Number of Mines [10, 20] or 'QUIT' to quit: ")
        if(uInput == "QUIT"):
            break
        try:
            mines = int(uInput)
            if(mines >= 10 and mines <= 20):
                myBoard = Board(mines)
                print("Start playing")
            else:
                raise ValueError #intended value error for when user inputs values less than 10 or greater than 20
        except:
            print("Not a valid integer value for mines")
            continue



        #wait for user to input on a cell (only allow left click, no flag for first click)
        #print board (can be done hopefully painlessly with numBombNeighbors in board class)
        while True:
            inputSelect = get_input()
            if inputSelect[0] != -1:
                break
        while True:
            if not inputSelect[2]:
                break
            else:
                print("Only a left click is allowed for your first move Try again")
                inputSelect = get_input()
        myBoard.populateBoard(inputSelect[0], inputSelect[1])
        print(myBoard)
        myBoard.setState(inputSelect[0], inputSelect[1])
        print(myBoard)


        while(myBoard.hasWon() == 0):
            #wait for user to input on a cell
            while True:
                inputSelect = get_input()
                if inputSelect[0] != -1:
                    break

            #print board (can be done hopefully painlessly with numBombNeighbors in board class)
            myBoard.setState(inputSelect[0], inputSelect[1], inputSelect[2])
            print(myBoard)


        result = myBoard.hasWon()
        if(result == -1):
            print("Game Over: You Lost.\nTry again?\n")
            #print board (can be done hopefully painlessly with numBombNeighbors in board class)
            #but this time display all mines and false flags, but keep covered spaces properly covered, likely done with getCellState in board class
        elif(result == 1):
            print("You Win! Play Again?\n")
        else:
            raise ValueError("An unexpected error occurred (hasWon returned {result})")
    print("Thanks for Playing")

main()