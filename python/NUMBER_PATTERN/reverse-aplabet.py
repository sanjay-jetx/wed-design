n=5
p=69
for i in range(n):
    for j in range(i+1):
        print(chr(p),end='')
    print()
    p-=1