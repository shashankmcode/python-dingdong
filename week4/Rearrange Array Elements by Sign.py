""" nums= [1,2,-4,-5]
n=len(nums)
pos=[]
neg=[]
for i in range(n):
    if nums[i]<0:
        neg.append(nums[i])
    else:
        pos.append(nums[i])
#now arrange them
for i in range(len(pos)):
    nums[2*i]=pos[i]
for i in range(len(neg)):    
    nums[2*i+1]=neg[i]
print(nums) """

#better
nums= [1,2,-4,-5]
n=len(nums)
pos=0  #starting +vs number
neg=1
ans=[None]*n
for i in range(n):
    if nums[i]>0:
        ans[pos]=nums[i]
        pos+=2
    else:
        ans[neg]=nums[i]
        neg+=2
print(ans)


