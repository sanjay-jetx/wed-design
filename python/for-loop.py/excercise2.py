number=input("enter the number : ")
number_1=number.split()
count=0
for i in number_1 :
    count=count+1
print(count)
for i in range(count):
    number_1[i]=int(number_1[i])
print(number_1)
max=number_1[0]
for i in number_1:
    if i > max :
        max= i
print(max)
 