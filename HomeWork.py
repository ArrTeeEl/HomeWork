from tkinter import *
from tkinter import filedialog, messagebox

def do():
    if (entry1.get() == "" or
        entry2.get() == "" or
        entry3.get() == "" or
        entry4.get() == "" or
        entry5.get() == "" or
        entry6.get() == ""):

        messagebox.showerror("Error", "Please fill in all the required fields.")
        return


    if not entry3.get().isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return


    if int(entry3.get()) < 18:
        messagebox.showerror("Error", "You must be at least 18 years old to register.")
        return

    messagebox.showinfo("Success", "Registration Successful!")
    clear_form()

def upload_document():
    file_path = filedialog.askopenfilename(
        title="Select Age Verification Document",
        filetypes=[("PDF files", "*.pdf"), ("Image files", "*.jpg;*.png"), ("All files", "*.*")]
    )
    if file_path:
        entry5.delete(0, END)
        entry5.insert(0, file_path)

def clear_form():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


window = Tk()
window.title("SportyBet")
window.geometry("700x600")
icon = PhotoImage(file="sportybet.png")
window.iconphoto(True, icon)
window.configure(background="#d1a5a5")
label=Label(window, text="SportyBet Registration Form",
             font=("Arial", 15),bg="#d1a5a5",
             bd=5,
             relief="raised",)
label.pack()


label1 = Label(window, text="First Name:", font=("Arial", 12))
label1.pack(pady=(10,0))

entry1 = Entry(window, width=30, font=("Arial", 12))
entry1.pack(pady=(0,10))

label2 = Label(window, text="Last Name:", font=("Arial", 12))
label2.pack(pady=(10,0))

entry2 = Entry(window, width=30, font=("Arial", 12))
entry2.pack(pady=(0,10))

label3 = Label(window, text="Age:", font=("Arial", 12),)
label3.pack(pady=(10,0))

entry3 = Entry(window, width=30, font=("Arial", 12))
entry3.pack(pady=(0,10))


label5 = Label(window, text="Age Verification:", font=("Arial", 12))
label5.pack(pady=(10,0))

entry5 = Entry(window, width=30, font=("Arial", 12))
entry5.pack(pady=(0,10))

upload_btn = Button(window, text="Upload Document", command=upload_document)
upload_btn.pack(pady=(0,0))

label7 = Label(window, 
               text="Note: Please add an appropriate document to verify your age", 
               font=("Arial", 10), 
               fg="red", 
               bg="#d1a5a5")
label7.pack(pady=(0,5))


label4 = Label(window, text="Email:", font=("Arial", 12))
label4.pack(pady=(10,0))

entry4 = Entry(window, width=30, font=("Arial", 12))
entry4.pack(pady=(0,10))


label6 = Label(window, text="Password:", font=("Arial", 12))
label6.pack(pady=(10,0))

entry6 = Entry(window, width=30, font=("Arial", 12), show="*")
entry6.pack(pady=(0,10))

button1 = Button(window, text="Register", 
                 font=("Arial", 10), 
                 bg="#d1a5a5",
                command=do,
                 fg="green")
button1.pack(pady=(10,0))



window.mainloop()

