def tenMultiplier(Num):
    return (Num * 10)

def hunMultipler(Num):
    return (Num * 100)

def thouMultipler(Num):
    return (Num * 1000)

def tthouMultipler(Num):
    return (Num * 10000)

def hunthouMultipler(Num):
    return (Num * 100000)

def milMultipler(Num):
    return (Num * 1000000)


print("Kilometre Units Converter")
print("1. Km to Hm")
print("2. Km to Dam")
print("3. Km to M")
print("4. Km to Dm")
print("5. Km to Cm")
print("6. Km to Mm")

choice = int(input("Choose an option (1-6): "))
Num=float(input("Enter Number To Convert; "))
while Num=="":
    print("Please Enter Numnber")
    Num=float(input("Enter Number To Convert; "))


if choice== 1 :
    print("Result:", tenMultiplier(Num),"hm")
elif choice== 2 :
    print("Result:", hunMultipler(Num),"dam")
elif choice== 3 :
    print("Result:", thouMultipler(Num),"m")
elif choice== 4 :
    print("Result:", tthouMultipler(Num),"dm")
elif choice== 5 :
    print("Result:", hunthouMultipler(Num),"cm")
elif choice== 6 :
    print("Result:", milMultipler(Num), "mm")
else:
    print("Invalid choice!")


