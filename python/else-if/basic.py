height=int(input("enter the height : "))
if(height>3):
    print("you are eligible for ride ")
    age=int(input("enter the age :"))
    if age<=18:
        print("pay 250")
    else:
        print("pay 500")
else:
    print("low height")