num = [3,5,1,10]
n=6
for i in range(len(num)):
    for j in range(1,len(num)):
        if num[i]+num[j]==n:
         print(i,j)


#Better
nums = [3,5,1,10]
target=6
nums.sort()#Sorts here
print(nums)
l,r=0,len(nums)-1
while l<r:
    cur_sum=nums[l]+nums[r]
    if cur_sum == target:
        print(l,r)
        break
    elif cur_sum<target:
        l+=1
    else:
        r-=1
print(l,r)

