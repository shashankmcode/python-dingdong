arr=[1,2,3,4,5]
n=len(arr)
temp=[]
for i in range(1,len(arr)):
    temp.append(arr[i])
temp.append(arr[0])
print(temp)

#using slice operations
arr=[1,2,3,4,5]
n=len(arr)
temp=[]
temp=arr[1:] # Copy all elements from index 1 to the end
temp.append(arr[0])
print(temp)

#using the same array
arr=[1,2,3,4,5]
n=len(arr)
temp=arr[0]
for i in range(1,len(arr)):
    arr[i-1]=arr[i]
arr[-1]=temp #replace the last element
print(arr)

#
arr=[1,2,3,4,5]
temp=arr[::-1] #reverse array
print(temp)
