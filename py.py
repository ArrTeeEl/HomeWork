import tkinter as tk
from tkinter import messagebox

def register():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()

    if not name or not email or not password or not gender:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Registration Successful!\nName: {name}\nEmail: {email}\nGender: {gender}")

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")

# Labels and Entry fields
tk.Label(root, text="Name").pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Email").pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

# Gender selection
tk.Label(root, text="Gender").pack(pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Register button
tk.Button(root, text="Register", command=register).pack(pady=20)

root.mainloop()
