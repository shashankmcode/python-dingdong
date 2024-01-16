rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end='')

    # Print asterisks
    for j in range(2 * i - 1):
        print("*", end='')

    # Move to the next line after each row
    print()
for i in range(rows, 0, -1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end='')

    # Print asterisks
    for j in range(2 * i - 1):
        print("*", end='')

    # Move to the next line after each row
    print()



