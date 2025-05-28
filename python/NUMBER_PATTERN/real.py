n = 5
for i in range(n):
    for j in range(i):  # Inner loop for spacing (optional)
        print(" ", end="")  # Printing spaces

    for j in range(i, n):  # Inner loop for printing numbers
        print(j, end="")  

    print()  # Move to the next line after finishing the row
