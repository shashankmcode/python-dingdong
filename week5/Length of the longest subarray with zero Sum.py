num=[9, -3, 3, -1, 6, -5]
n=len(num)
ans=0
for i in range(n):
    temp=0
    for j in range(i,n):
       temp+=num[j]#from i to j length
       if temp==0:
           length=j-i+1
           if length>ans:
               ans=length
print(ans)
