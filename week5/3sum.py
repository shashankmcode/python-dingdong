#brute
num=[-1,0,1,2,-1,-4]
n=len(num)
result=set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if num[i]+num[j]+num[k]==0:
                result.add(tuple(sorted((num[i],num[j],num[k]))))
print(result)
#set me list add nai karsakta so tuple ko convert

#optimal approach
num=[0,0,0]
num.sort()
n=len(num)
sum=float('inf')
result=[]
for i in range(n):
    if i>0 and num[i]==num[i-1]:
        continue
    j= i+1
    k=n-1
    while(j<k):
        sum=num[i]+num[j]+num[k]
        if sum<0:
            j+=1
        elif sum>0:
            k-=1
        else:
            temp=num[i],num[j],num[k]
            result.append(temp)
            j+=1
            k-=1
            while(j < k and num[j]==num[j-1]): j+=1 #to remove duplicates
            while(j < k and num[k]==num[k+1]): k-=1
print(result)