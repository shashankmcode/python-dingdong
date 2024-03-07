num=[3, 1, 2, 4]
n=len(num)
k=6
count=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=num[j]
        if sum==k:
            count+=1
print(count)
