
"""
Author: Maha Jornaz and Pheonix Brehm, Created 9/14/26
Last updated: 9/19/26 - by Maha Jornaz
Code is authored by Maha Jornaz, with Phoenix Brehm adding the left/right click mode and changing the error returns.
The goal of the input handler was to get the cell that the user selected, ensure the user's input is correct, and to determine the user's action.
Functions implemented are:
    get_input: 
        - getting the user's cell input
        - getting the left/right click mode
        - verifying the user's input
        - converting the user-friendly coordinates to the program's internal coordinates
        - returning the results
"""



def get_input():
    # gets the user's cell input and click mode
    user_input_cell_location = input("Enter a cell: ").upper().strip()
    user_input_click_mode = input("Enter L (for left clicking) or R (for right clicking): ").upper().strip()

    col_letters = "ABCDEFGHIJ"     # stores the column letters

    if len(user_input_cell_location) < 2:      # checks the user's characters if its sufficient for the cell
        print("Error: Empty input")
        return (-1, -1, False)


    if user_input_cell_location[0] not in col_letters:     # checks the first character if its a valid column letter
        print("Error: Invalid column or order")
        return (-1, -1, False)


    if not user_input_cell_location[1:].isdigit():    # checks the characters after the column are digits
        print("Error: Non-number row")
        return (-1, -1, False)

    if user_input_click_mode != "L" and user_input_click_mode != "R":   # checks if the left/right click is valid
        print("Error: No proper click mode specified")
        return (-1, -1, False)
    
    row = int(user_input_cell_location[1:]) - 1    # the user's 1-10 row input gets converted to a 0-9 index
    
    if row < 0 or row > 9:         # checks whether the row is within the bounds 
        print("Error: Row out of bounds")
        return (-1, -1, False)
    
    
    column = col_letters.index (user_input_cell_location[0])    # the user's column letter get converted to a 0-9 index

    # the user's left/right click mode get converted to false/true
    if user_input_click_mode == "L":     
        mode = False
    if user_input_click_mode == "R":
        mode = True
    return (row, column, mode)


#selection = (get_input())      [used to debug/test]

#if selection != False: 
    #(row, column) = selection

#print(selection)
