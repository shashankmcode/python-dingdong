row=5
space=8
for i in range(1,row+1):
    for j in range(1,i+1):
        print('*',end=' ')
    #print()
    for j in range(1,space+1):
        print(' ',end=' ')
    space-=2
    #print()
    for j in range(1,i+1):
        print('*',end=' ')
    print()
space=2
for i in range(row,0,-1):
    for j in range(1,i+1-1):
        print('*',end=' ')
    #print()
    for j in range(1,space+1):
        print(' ',end=' ')
    space+=2
    for j in range(1,i+1-1):
        print('*',end=' ')
    print()