row=int(input('enterr the rows'))
colum=int(input('enterr the colums'))

martrix=[]
for Row in range(row):
    a=[]
    for col in range(colum):
        temp=int(input())
        a.append(temp)
    martrix.append(a)
print(martrix)