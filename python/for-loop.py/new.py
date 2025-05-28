total_sum = 0  # Initialize the sum

# Read 10 numbers and add each to the sum
for i in range(10):
    num = int(input("Enter a number: "))
    print(num)  # Print the entered number
    total_sum += num  # Add the entered number to the sum

print("The sum of the numbers is:", total_sum)
