import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from ttkthemes import ThemedTk

add = ''
result = ''
clear_display = False

def button_click(number):
    global add
    global result
    global clear_display
    
    try:
        if number == 'AC':
            add = ''
            result = ''
        elif number in ['/', '×', '-', '+']:
            if number == '×':
                number = '*'
            add += number
            result += number
            clear_display = False
        elif number == 'CE':
            add = add[:-1]
            result = result[:-1]
        elif number == '=':
            add = str(eval(result))
            result = add
            if float(result).is_integer():
                add = str(int(eval(result)))
            clear_display = True
        else:
            if clear_display:
                add = number
                result = number
                clear_display = False
            else:
                add += number
                result += number
    except Exception as e:
        add = result = '0'
    finally:
        box.delete(0, tk.END)
        box.insert(0, add)

class Calculator:
    def __init__(self, text, row, column):
        self.text = text
        self.row = row
        self.column = column

    def press(self):
        button = ttk.Button(root, text=self.text, command=lambda: button_click(self.text))
        button.grid(row=self.row, column=self.column, sticky='nsew')

if __name__ == '__main__':
    root = ThemedTk(theme="yaru")
    root.title("Calculadora")
    root.resizable(0,0)

    box = ttk.Entry(root, width=30)
    box.grid(column=0, row=0, columnspan=4, ipady=10)

    custom_font = tkFont.Font(family="Helvetica", size=14)
    box.configure(font=custom_font)

    buttons = [
        ('(', 1, 0), (')', 1, 1), ('CE', 1, 2), ('AC', 1, 3),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('×', 3, 3), 
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
    ]

    for (text, row, column) in buttons:
        button = Calculator(text, row, column)
        button.press()

    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)

    root.mainloop()
