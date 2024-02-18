nums=[2,0,2,1,1,0]
n=len(nums)
one=0
two=0
zero=0
for i in range(len(nums)):
    if nums[i]==0:
        zero+=1
    elif nums[i]==1:
        one+=1
    else:
        two+=1
print(zero,one,two)
for i in range(zero):
    nums[i] = 0

for i in range(zero, zero + one):
    nums[i] = 1

for i in range(zero + one,n):
    nums[i] = 2
print(nums)
#or use slice operation
num=[]
num[:] = [0] * zero + [1] * one + [2] * two
print(num)