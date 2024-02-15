#Works for sorted array
num = [1,2,3,4,5,7]
for i in range(len(num)-1):
    if num[i]+1==num[i+1]:
        continue
    else:
        print(num[i]+1)
#best solution
num = [0,1]
one=0
two=0
for i in range(len(num)+1):     #zero he agar toh start from 0 varna for i in range(1,len(num)+1)
    one=one^i
for i in range(len(num)):
    two=two^num[i]
result=one^two
print(result)
    