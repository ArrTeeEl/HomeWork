import tkinter as tk

calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    pass

def clear_calculation():
    pass

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")

text_result = tk.Text(root, height=2, width=22, font=("Gothic ", 24))
text_result.grid(columnspan=5)



root.mainloop()
