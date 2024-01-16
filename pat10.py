row=5
for i in range(1,row+1):
    for j in range(0,i):
        print('*',end='')
    print()
for i in range(row,0,-1):
    for j in range(0,i):
        print('*',end='')
    print()

