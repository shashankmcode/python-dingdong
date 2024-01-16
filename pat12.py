row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(2*row-2*i):
         print(" ",end = " ")
    for l in range(i, 0, -1):
        print(l, end=" ")
    print()





