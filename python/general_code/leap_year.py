year=int(input("enter the year : "))
if year%4 == 0 :
    if year%100 :
        if year%400 :
            print("it is leap year")
else: 
    print("it is not leap year")