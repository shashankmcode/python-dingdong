nums = [3,2,1]
n=len(nums)
ind=-1
for i in range(n-2,-1,-1):
    if nums[i]<nums[i+1]:
       ind=i
       break
print(ind)
if ind==-1: 
 nums.reverse()
else:
 for i in range(n-1,ind,-1):
    if nums[i]>nums[ind]:
        nums[i],nums[ind]=nums[ind],nums[i]
        #print(nums)
        break
 nums[ind+1:n+1]=reversed(nums[ind+1:n+1]) #reverse 
print(nums)
#print(ind)