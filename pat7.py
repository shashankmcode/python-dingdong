rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(rows-i-1):
        print(" /", end='')
    for j in range(2*i+1):
        print("* ", end='')
    for j in range(rows-i-1):
        print(" ", end='')
    print()

        
    
          

