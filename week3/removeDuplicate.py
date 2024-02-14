#Space complexity increase version because we are using the another array here
arr=[1,1,1,2,2,3,3,3,3,4,4]
n=len(arr)
temp=[]
temp.append(arr[0])
for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]:
     temp.append(arr[i])
print(temp)

#Arrangeing the elements in the existing array itself
arr=[1,1,2]
n=len(arr)
j=1
for i in range(1,len(arr)):
    if arr[i]!=arr[j]:
        j+=1
        arr[j]=arr[i]
print(j)
print(arr)
    