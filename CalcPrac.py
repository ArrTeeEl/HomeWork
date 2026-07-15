from tkinter import *

def add():
    result.config(text=int(num1.get()) + int(num2.get()))

def subtract():
    result.config(text=int(num1.get()) - int(num2.get()))

def multiply():
    result.config(text=int(num1.get()) * int(num2.get()))

def divide():
    result.config(text=int(num1.get()) / int(num2.get()))

root = Tk()

num1 = Entry(root)
num2 = Entry(root)
num1.pack()
num2.pack()

button =Button(root, text="Add", command=add)
button.pack()

button =Button(root, text="Subtract", command=subtract)
button.pack()

button =Button(root, text="Multiply", command=multiply)
button.pack()

button =Button(root, text="Divide", command=divide)
button.pack()

result =Label(root)
result.pack()
root.mainloop()
