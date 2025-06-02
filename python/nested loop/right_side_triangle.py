n = 5
for i in range(n):
    for j in range(i, n):  # Prints spaces to align the stars
        print(" ",end="")  
    for j in range(i + 1):  # Prints stars
        print("*", end="")  
    print()  # Moves to the next line