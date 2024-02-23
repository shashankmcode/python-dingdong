nums = [10, 22, 12, 3, 0, 6]
n=len(nums)
temp=0
for i in range(n):
    leader=True
    for j in range(i+1,n):
        if nums[j]>nums[i]:
            leader=False
            break
    if leader==True:
            temp=nums[i]
            print(temp)   
#better
nums = [10, 22, 12, 3, 0, 6]
n=len(nums)
max=0
temp=[]
for i in range(n-1,-1,-1):
     if nums[i]>max:
          temp.append(nums[i])
          max=nums[i]
print(temp)
