arr=[1,2,3,4,5]
temp=0
for i in range(0,len(arr)):
    if arr[i]>temp:
        temp=arr[i]
print(temp)