rows = int(input("Enter the number of rows: "))
for _ in range(1,rows+1):
    for j in range(0,rows-_+1):
        print('*',end='')
    print()