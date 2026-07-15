import tkinter as tk

# Global variable to store the calculation
calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Text widget to display results
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Buttons
buttons = [
    ('1', 1, 1), ('2', 1, 2), ('3', 1, 3), ('+', 1, 4),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('-', 2, 4),
    ('7', 3, 1), ('8', 3, 2), ('9', 3, 3), ('*', 3, 4),
    ('C', 4, 1), ('0', 4, 2), ('=', 4, 3), ('/', 4, 4),
]

for (text, row, col) in buttons:
    if text == "=":
        action = evaluate_calculation
    elif text == "C":
        action = clear_field
    else:
        action = lambda x=text: add_to_calculation(x)
    tk.Button(root, text=text, width=5, height=2, command=action).grid(row=row, column=col)

# Run the application
root.mainloop()
