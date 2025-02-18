a=int(input("enter the mrk A : "))
b=int(input("enter the mrk B : "))
c=int(input("enter the mrk C : "))
d=int(input("enter the mrk D : "))
e=int(input("enter the mrk E : "))
add=a+b+c+d+e
print("total marks : ",add)
avg=add/5
print("avg marks :",avg)
if(avg<35):
    print("additional class required ")
else:
    print("you r good to go")