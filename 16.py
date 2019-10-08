P= int(input("Enter principle: "))

T = int (input("Enter time: "))

R = int (input("Enter rate: "))

CI =  P * pow((1 + R / 100), T)


print("Compound Interest = ", CI)
