salary=int(input("enter the salary : "))
age=int(input("enter the age :"))
if(salary>=20000 or age<=25):
    loan=int(input("enter the loan amount : "))
    if(loan>=50000):
        print("u r not eligible")
    else:
        print("u r eligible for loan")
else:
    print("u r not eligible for loan") 