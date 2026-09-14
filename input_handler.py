
def get_input():
    user_input = input("Enter a cell: ").upper().strip()

    col_letters = "ABCDEFGHIJ"

    if len(user_input) < 2:
        print("Error: Empty input")
        return False


    if user_input[0] not in col_letters:
        print("Error: Invalid column or order")
        return False


    if not user_input[1:].isdigit():
        print("Error: Non-number row")
        return False

    
    row = int(user_input[1:]) - 1
    if row < 0 or row > 9:
        print("Error: Row out of bounds")
        return False
    
    
    column = col_letters.index (user_input[0])
    return (row, column)


#selection = (get_input())      [used to debug/test]

#if selection != False: 
    #(row, column) = selection

#print(selection)
