#brute force
arr = [1,2,0,0,3,4,0,5]
n = len(arr)
temp=[]
for i in range(len(arr)):
    if arr[i]!=0:
        temp.append(arr[i])
remaining=n-len(temp)
temp= temp+[0]*remaining
print(temp)

#better solution
arr = [0,1,0]
n = len(arr)
j=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print(arr)

#more enhanced
arr = [1,2,0,0,5]
n = len(arr)
for i in range(len(arr)):
    if arr[i]==0:
        arr.append(0)
        arr.remove(arr[i])
print(arr)
