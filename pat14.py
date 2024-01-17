row=5

for i in  range(1,row+1):
    num=ord('A')
    for j in range(1,i+1):
        print(chr(num),end=' ')
        num+=1
    print()