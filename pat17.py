""" row=5
for i in range(1,row+1):
    for j in range(row-i):
        print('/',end=' ')
    char=ord('A')
    brea=(2*i+1)//2
    for j in range(1,2*i):
        print(chr(char),end=' ')
        if brea<j:
            char+=1
        else:
            char-=1
    for j in range(row-i):
        print('/',end=' ')
    print() """
        
N = 6

for i in range(1, N + 1):
    # Print leading spaces
    for j in range(N-i):
        print('/', end='')

    # Print increasing characters
    for k in range(i):
        print(chr(ord('A') + k), end='')

    # Print decreasing characters
    for l in range(i - 2, -1, -1):
        print(chr(ord('A') + l), end='')

    # Move to the next line
    print()
