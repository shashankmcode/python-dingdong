num=[1,0,-1,0,-2,2]
n=len(num)
result=set()#declaration of empty set
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if  num[i]+num[j]+num[k]+num[l]==0:
                    result.add(tuple(sorted((num[i],num[j],num[k],num[l]))))

#print(result)
#optimal same logic as 3sum
num=[1,0,-1,0,-2,2]
num.sort()
n=len(num)
target=0
result=[]
temp=[]
sum=float('inf')
for i in range(n):
    if i>0 and num[i]==num[i-1]:
        continue
    for j in range(i+1,n):
        if j!=i+1 and num[i]==num[i-1]:
            continue
        k= j+1
        l=n-1
        while(k<l):
            sum=num[i]+num[j]+num[k]+num[l]
            if sum==target:
                temp=num[i],num[j],num[k],num[l]
                result.append(temp)
                k+=1
                l-=1
                while(num[k]==num[k-1]):k+=1#to handel duplictes
                while(num[l]==num[l+1]):l-=1
            elif sum < target:
                k+=1
            else:
                l-=1

                    
print(result)
