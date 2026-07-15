Password=input("Enter your password: ")
while Password != "admin123":
    print("Access Denied. Try again.")
    Password = input("Enter your password: ")
print("Access Granted. Welcome!")