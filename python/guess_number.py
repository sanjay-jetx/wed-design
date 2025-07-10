unique_number=58
chance=6
for i in range(chance):
    number=int(input("enter the number :"))
    if(number==unique_number):
        print("you win")
    elif(number>unique_number):
        print("unique value is less than ",number)
    elif(number<unique_number):
        print("unique value is greather than",number)
    else:
        print("you failed")       
print("game over")