d= int(input("Enter days:  "))

years = int (d/365)
weeks = int ((d - (years* 365))  / 7)

days = int (d - ((years * 365) + (weeks * 7)))

print(d, "days = ", years  ,"years" ,     weeks, "weeks",    days, "days")







                   
