num = [-1]

max_sum=0
max_subarray=[]
for i in range(len(num)):
    sum=0
    for j in range(i,len(num)):
        sum+=num[j]
        if(sum>max_sum):
         max_sum=sum
         max_subarray = num[i:j + 1]
         
print(max_sum)
print(max_subarray)

#better approacah
num = [-2,1,-3,4,-1,2,1,-5,4]
sum=0
max_sum=0
start=0
end=0
temp=[]
for i in range(len(num)):
   if sum==0:
      start=i
   sum+=num[i]
   if sum>max_sum:
      max_sum=sum
      end=i
   if sum<0:
      sum=0
temp=num[start:end]
print(max_sum)
print(temp)
      
   
   
   

""" maxi=-sys.maxsize-1
n=len(nums)
sum1=0
for i in range(n):
sum1+=nums[i]
if(sum1>maxi):
maxi=sum1
if(sum1<0):
sum1=0
return maxi """

        