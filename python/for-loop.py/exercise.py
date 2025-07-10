height=input("enter the height")  
height_list=height.split()
count=0
for i in height_list:
    count=count+1
print(count)
total=0
for i in range(count):
    height_list[i]=int(height_list[i])
print(height_list)  

for i in height_list :
    total+=i
print(total)

