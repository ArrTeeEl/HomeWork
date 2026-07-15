#Area Ya SKWEA.
#Calculator
Operator=input("Enter mode of Operation (+, -, *, /); ")
while Operator=="": 
    print("This is Required Bro")
    Operator=input("Enter mode of Operation (+, -, *, /); ")


Number1=float(input("Insert First number; "))
while Number1=="":
    print("This is Required too Bro")
    Operator=float(input("Insert First number; "))

Number2=float(input("Insert Second number; "))
while Number2=="": 
    print("This is Required TOO Bro")
    Operator=float(input("Insert Second number; "))

if Operator=="+":
    print(Number1 + Number2)
elif Operator=="-":
    print(Number1 - Number2)
elif Operator=="*":
    print(Number2 * Number1)
elif Operator=="/":
    print(Number1 / Number2)

