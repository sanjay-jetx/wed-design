marks=int(input("enter the marks"))
if(marks<35):
    print("low marks")
elif(marks>35 and marks<=80):
    print("avg marks")
elif(marks>80 and marks<100):
    print("spr marks")
else:
    print("invalid inoput")