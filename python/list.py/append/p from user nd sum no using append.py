numbers = [] 
total_sum = 0
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
    print(num)
    total_sum += num

print("The sum of the numbers is:", total_sum)
