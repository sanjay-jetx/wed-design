import random
unique_number=random.randint(1,100)
chance=6
for i in range(chance):
    try:
     number=int(input("enter the number :"))
     if(number==unique_number):
        print("you win")
     elif(number>unique_number):
        print("unique value is less than ",number)
     elif(number<unique_number):
        print("unique value is greather than",number)
     else:
        print("you failed")  
    except ValueError:
        print("invalid guessed number")  
print("game over")