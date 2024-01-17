row=5
space=0
for i in range(1,row+1):
    for j in range(row-i+1):
        print('*',end=' ')
    for m in range(0,space):
        print(' ',end=' ') 
    space+=2
    for k in range(row-i+1):
        print('*',end=' ')
        
    print()
 
#space=

