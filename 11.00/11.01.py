import tkinter as tk

# Function to update the expression in the entry widget
def button_click(item):
    global expression
    expression += str(item)
    equation.set(expression)

# Function to evaluate the final expression
def button_equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the expression
def button_clear():
    global expression
    expression = ""
    equation.set("")

# Creating the main window
root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

expression = ""
equation = tk.StringVar()

# Creating the entry widget
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20, 'bold'), bd=5, insertwidth=4, width=15, justify='right')
entry.grid(row=0, columnspan=4)

# Creating buttons
button_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in button_list:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12, 'bold'), command=button_equal).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12, 'bold'), command=button_clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12, 'bold'), command=lambda x=button: button_click(x)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
