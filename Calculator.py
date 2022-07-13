# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:14:08 2022

@author: JamesIocco
"""

import tkinter as tk

calc = tk.Tk()
calc.title("Calculator")
   #button set up
buttons = [
'7',  '8',  '9',  '*',  'C',
'4',  '5',  '6',  '/',  ' ',
'1',  '2',  '3',  '-', ' ',
'0',  '.',  '=',  '+',   ' ']

# gui
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(calc, text = i, width = 7, height = 7, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = tk.Entry(calc, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)

def click_event(key):

	# = calculations
    if key == '=':
        # safeguard against integer division
        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")
			
        # evaluate result
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "   Error, use only valid chars")
			
	# C = clear		
    elif key == 'C':
        display.delete(0, tk.END)
		
		

	# clear and start new
    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)

# running the calculator
calc.mainloop()