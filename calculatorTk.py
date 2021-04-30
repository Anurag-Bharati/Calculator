
from tkinter import *

expression = ''

border_color = "#1A1A1D"
grid_color = "#950740"
c_equal = "#6F2232"
c_sign = "#6F2232"
c_clear = "#C3073F"

button_style = "raised"
button_border_size = 5
button_height = 3
button_width = 8
button_font = "cambria", "BOLD"
font_color = "#FFFFFF"
on_hover = "heart"

SCREEN = Tk()

SCREEN.geometry('400x700')  # Window size

SCREEN.title('Nice Calculator')

SCREEN.iconbitmap('calc.ico')   # File must be next to the .py file and the file extension must be .ico

SCREEN.configure(bg = border_color)     # Setting up a border color

SCREEN.resizable(False, False)

button_frame = Frame(SCREEN, bg = border_color)
button_frame.pack()

user_input = StringVar()    # Container to hold values
user_input.set('0')

SCREEN.mainloop()
