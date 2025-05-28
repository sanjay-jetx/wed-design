# This program prints a number pattern

# Outer loop controls the number of rows
for i in range(1, 5):
 # Start a new line for each row
    print()
    # Inner loop: prints the value of 'i' exactly 'i' times
    for j in range(1, i+1):
        print(i,end="")  # Print the current value of 'i' on the same line

