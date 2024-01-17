""" 
F
E F
D E F
C D E F
B C D E F
A B C D E F
 """
row=5
for i in range(1,row+1):
    #char=ord('')
    for j in range(1,i+1):
        print('*',end=' ')
    print()

N = 26

for i in range(N, 0, -1):
    for j in range(N, i - 1, -1):
        print(chr(ord('A') + j - 1), end=' ')
    print()
