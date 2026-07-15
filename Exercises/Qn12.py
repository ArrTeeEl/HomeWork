Check=int(input("Enter a number: "))
while Check=="":
    print("Please enter a number")
    Check=int(input("Enter a number: "))
if Check % 2 == 0:
        print("The number is even")
else:
        print("The number is odd")