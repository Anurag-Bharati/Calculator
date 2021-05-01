import random
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


def press(num):
    global expression

    expression = expression + str(num)
    user_input.set(expression)


def on_equal():
    try:
        global expression

        total = str(eval(expression))   # eval()  evaluate arbitrary Python expressions from a string-based input
        user_input.set(total)

        expression = ''

    except:
        user_input.set(' error ')
        expression = ''


def clear():
    global expression
    expression = ''
    user_input.set('0')  # Setting val to 0 when Clear


calc_display = Entry(button_frame, textvariable = user_input, justify = 'right', bd = button_border_size,
                     font = ('arial', 20, 'bold'), bg = "#4E4E50", fg = "#C3073F")
calc_display.grid(row = 0, column = 0, ipadx = 18, columnspan = 6, ipady = 25, pady = 40)

button1 = Button(button_frame, font = (button_font, 12), text = ' 1 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(1))
button1.grid(row = 1, column = 0)

button2 = Button(button_frame, font = (button_font, 12), text = ' 2 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(2))
button2.grid(row = 1, column = 1)

button3 = Button(button_frame, font = (button_font, 12), text = ' 3 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(3))
button3.grid(row = 1, column = 2)

plus = Button(button_frame, font = (button_font, 12), text = ' + ', bd = button_border_size, relief = button_style,
              fg = font_color, bg = c_sign, height = button_height, width = button_width, command = lambda: press("+"))
plus.grid(row = 1, column = 3)

button4 = Button(button_frame, font = (button_font, 12), text = ' 4 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(4))
button4.grid(row = 2, column = 0)

button5 = Button(button_frame, font = (button_font, 12), text = ' 5 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(5))
button5.grid(row = 2, column = 1)

button6 = Button(button_frame, font = (button_font, 12), text = ' 6 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(6))
button6.grid(row = 2, column = 2)

minus = Button(button_frame, font = (button_font, 12), text = ' - ', bd = button_border_size, relief = button_style,
               fg = font_color, bg = c_sign, height = button_height, width = button_width, command = lambda: press("-"))
minus.grid(row = 2, column = 3)

button7 = Button(button_frame, font = (button_font, 12), text = ' 7 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(7))
button7.grid(row = 3, column = 0)

button8 = Button(button_frame, font = (button_font, 12), text = ' 8 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(8))
button8.grid(row = 3, column = 1)

button9 = Button(button_frame, font = (button_font, 12), text = ' 9 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(9))
button9.grid(row = 3, column = 2)

multiply = Button(button_frame, font = (button_font, 12), text = ' * ', bd = button_border_size, relief = button_style,
                  fg = font_color, bg = c_sign, height = button_height, width = button_width,
                  command = lambda: press("*"))
multiply.grid(row = 3, column = 3)

button0 = Button(button_frame, font = (button_font, 12), text = ' 0 ', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press(0))
button0.grid(row = 4, column = 0)

decimal = Button(button_frame, font = (button_font, 12), text = '.', bd = button_border_size, relief = button_style,
                 fg = font_color, bg = grid_color, height = button_height, width = button_width,
                 command = lambda: press('.'))
decimal.grid(row = 4, column = 1)

clear = Button(button_frame, font = (button_font, 12), text = 'C', bd = button_border_size, relief = button_style,
               fg = font_color, height = button_height, width = button_width, bg = c_clear, command = clear)
clear.grid(row = 4, column = 2)

divide = Button(button_frame, font = (button_font, 12), text = ' / ', bd = button_border_size, relief = button_style,
                fg = font_color, bg = c_sign, height = button_height, width = button_width,
                command = lambda: press("/"))
divide.grid(row = 4, column = 3)

equal = Button(button_frame, font = (button_font, 12), text = ' = ', bd = button_border_size, relief = button_style,
               fg = font_color, bg = c_equal, command = on_equal, height = button_height, cursor = on_hover)
equal.grid(sticky = 'ewns', row = 5, column = 0, columnspan = 4, pady = 10)

text_message = Text(SCREEN, yscrollcommand = True, bg = border_color, fg = "#FFFFFF", pady = 5, padx = 2, bd = 5,
                    height = 5,
                    width = 45, cursor = "mouse")

Tips = ["Use the scroll wheel to move up/down.", "Press enter to change the line.", "Use arrow keys to navigate.",
        "You can erase me :(", "Select by left click and drag.", "Made with <3 by Anurag 210030 :P"]
text_message.insert(INSERT, "Your notes here!\n"
                            f"Tip: {Tips[random.randint(0, 5)]} \n\n\n\nBruh")
text_message.pack()


SCREEN.mainloop()
