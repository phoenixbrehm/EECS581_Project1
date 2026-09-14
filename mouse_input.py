
import tkinter


def clicked_cell(row, column):
    selection = (row, column)      #used to debug/test
    print(selection)
    

window = tkinter.Tk()

for x in range(0, 10):
    for y in range(0, 10):
        button = tkinter.Button(window, command=lambda r = x, c = y: clicked_cell(r, c))  
        button.grid(row = x, column = y)


window.mainloop()
