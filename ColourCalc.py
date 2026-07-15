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
root.configure(bg="#2E4053")  # Dark background

# Text widget to display results
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="#FDFEFE", fg="#1C2833")
text_result.grid(columnspan=5)

# Buttons with colours
buttons = [
    ('1', 1, 1, "#AED6F1"), ('2', 1, 2, "#AED6F1"), ('3', 1, 3, "#AED6F1"), ('+', 1, 4, "#F5B7B1"),
    ('4', 2, 1, "#A9DFBF"), ('5', 2, 2, "#A9DFBF"), ('6', 2, 3, "#A9DFBF"), ('-', 2, 4, "#F5B7B1"),
    ('7', 3, 1, "#F9E79F"), ('8', 3, 2, "#F9E79F"), ('9', 3, 3, "#F9E79F"), ('*', 3, 4, "#F5B7B1"),
    ('C', 4, 1, "#E74C3C"), ('0', 4, 2, "#AED6F1"), ('=', 4, 3, "#58D68D"), ('/', 4, 4, "#F5B7B1"),
]

for (text, row, col, color) in buttons:
    if text == "=":
        action = evaluate_calculation
    elif text == "C":
        action = clear_field
    else:
        action = lambda x=text: add_to_calculation(x)
    tk.Button(root, text=text, width=5, height=2, command=action, bg=color, fg="black").grid(row=row, column=col)

# Run the application
root.mainloop()
