import math

num = int(input("Enter a number: "))
while num < 0: 
    print("Please enter a non-negative number")
    num = int(input("Enter a number: "))
print(round(math.sqrt(num), 4))