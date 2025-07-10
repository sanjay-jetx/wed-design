for i in range(5):
    for j in range(i, 5):  # Prints decreasing '*' pattern
        print("*", end="")
    for j in range(i + 1):  # Prints spaces without moving to a new line
        print(" ",end="")
    print()  # Moves to the next line
