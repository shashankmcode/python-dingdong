row=5
space=0
for i in range(1,row+1):
    for j in range(row-i+1):
        print('*',end=' ')
    for j in range(0,space):
        print(' ',end=' ') 
    space+=2
    for j in range(row-i+1):
        print('*',end=' ')
        
    print()
 
space=8
for i in range(row,0,-1):
    for j in range(1,row-i+2):
        print('*',end=' ')
    #print()
    for j in range(1,space+1):
        print(' ',end=' ')
    space-=2
   # print()
    for j in range(1,row-i+2):
        print('*',end=' ')
    print()