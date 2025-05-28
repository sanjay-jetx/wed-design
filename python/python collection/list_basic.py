a=[1,2,3,4]
b=[11,23,34,54,65]
print(type(a))
print(a)
a.append(10)
a.append(100)
a.append("hi")
print(a)
print(a[0])
print(a[1],a[2]) 
a.insert(0,"hi") #insert the number INSERT
print(a)
a[1]=10 #replace the number
a.pop(3) #removing the number POP
print(a)
a.extend(b) #join the a and b
print(a)
c=(23,34,54)
d=list(c) #we can change the tuple into list
d.append(7865)
print(d)
print(c)