row=5
for i in  range(1,row+1):
    for j in range(1,i+1):
        char=ord('A')
        char=chr(char+i-1)
        print(char,end=' ')
        
    print()