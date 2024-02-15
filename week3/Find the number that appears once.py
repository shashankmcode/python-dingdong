num = 4,1,2,1,2
n = len(num)
for i in range(n):
    test=False
    for j in range(n):
        if  num[j]==num[i]:
            test=True
            break
    if test==False:
        print(num[i])

        
        


