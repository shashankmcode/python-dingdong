nums=[2,2,1,1,1,2,2]
n=len(nums)

for i in range(n):
    count=0
    for j in range(i,n):
        if nums[i]==nums[j]:
            count+=1
    if(count>n/2):
        print(nums[i])
        break