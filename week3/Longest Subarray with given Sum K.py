num = 2,3,5,1,7,1,1
n=10
max_temp=0
for i in range(len(num)):
    sum=0
    for j in range(i,len(num)):
        sum+=num[j]
        if sum==n:
            temp=j-i+1
            if temp>max_temp:
                max_temp=temp
print(max_temp) #printss after poora n length dekhne ke baad


#best
num = 2,3,5,1,7,1,1
n=10
temp=0
maxt=0
sum=num[0]
for i in range(len(num)):
    for j in range(i,len(num)):
        if sum<=n:
         sum+=num[j]
         temp=j-i+1
         if temp > maxt:
             maxt=temp
print(temp)

            