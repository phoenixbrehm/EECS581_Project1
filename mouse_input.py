# tkinter for the buttons and images.
import tkinter as tk
# PIL for image resizing.
from PIL import Image, ImageTk

# Makes the window for the grid at the bottom two for loop.
window = tk.Tk()

""" 
Grabs the image from the image folder and resises it to match the size of the buttons. (test with other images if wanted like bombs).
Image must be resized because it would scale the button the image size instead.
button_image makes use of the resized image.
blank_image is used to make the buttons blank at the start of the game, but also makes it so the width and height parameters are in pixels.
"""
original_image = Image.open("images/MINESWEEPER_FLAG.png")
resized_image = original_image.resize((32, 32), Image.Resampling.NEAREST)
button_image = ImageTk.PhotoImage(resized_image)
blank_image = tk.PhotoImage(width=1, height=1)

# Maha's clicked_cell function.
def clicked_cell(row, column):
    # Gets the row and column of the button and then prints it in the terminal.
    selection = (row, column)      #used to debug/test
    print(selection)

# Left click function that changes the color of the background of the button to light gray.
def left_click(event):
    event.widget.configure(bg="light gray")

# Right click function that changes the image of the button to the flag image.
def right_click(event):
    event.widget.configure(image=button_image)
    event.widget.image = button_image

# Maha's double for loop for creating the blank button grid.
for x in range(0, 10):
    for y in range(0, 10):
        button = tk.Button(window, image=blank_image, width=32, height=32, command=lambda r = x, c = y: clicked_cell(r, c))  
        button.grid(row = x, column = y)
        # Ethan Le's left and right click functions that are binded to the buttons.
        button.bind("<Button-1>", left_click)
        button.bind("<Button-3>", right_click)

# Lets you press the buttons as many times as you want until you close the window.
window.mainloop()
