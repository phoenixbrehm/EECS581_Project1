
def get_input():
    user_input_cell_location = input("Enter a cell: ").upper().strip()
    user_input_click_mode = input("Enter L (for left clicking) or R (for right clicking): ").upper().strip()

    col_letters = "ABCDEFGHIJ"

    if len(user_input_cell_location) < 2:
        print("Error: Empty input")
        return (-1, -1, False)


    if user_input_cell_location[0] not in col_letters:
        print("Error: Invalid column or order")
        return (-1, -1, False)


    if not user_input_cell_location[1:].isdigit():
        print("Error: Non-number row")
        return (-1, -1, False)

    if user_input_click_mode != "L" and user_input_click_mode != "R":
        print("Error: No proper click mode specified")
        return (-1, -1, False)
    
    row = int(user_input_cell_location[1:]) - 1
    if row < 0 or row > 9:
        print("Error: Row out of bounds")
        return (-1, -1, False)
    
    
    column = col_letters.index (user_input_cell_location[0])
    if user_input_click_mode == "L":
        mode = False
    if user_input_click_mode == "R":
        mode = True
    return (row, column, mode)


#selection = (get_input())      [used to debug/test]

#if selection != False: 
    #(row, column) = selection

#print(selection)
