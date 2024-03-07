nums = [1,2,-3,0,-4,-5]
[1,1,1]

pre=1
suf=1
maxi=1

for i in range(len(nums)):
        
    pre=pre*nums[i]
    suf=suf*nums[len(nums)-i-1]
    if nums[i]==0:
        pre=1
    maxi=max(maxi,suf,pre)

print(maxi)
