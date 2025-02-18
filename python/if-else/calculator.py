a=int(input("enter the number :"))
b=int(input("enter the number :"))
operation=input("add/sub/multi/div")
if(operation=="add"):
    print("a+b =",a+b)
elif(operation=="sub"):
    print("a-b",a-b)
elif(operation=="multi"):
    print("a*b",a*b)
elif(operation=="div"):
    print("a/b",a/b)
else:
    print("invalid input")