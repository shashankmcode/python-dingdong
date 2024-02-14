#brute force approach
arr=[1,2,3]
n=len(arr)
sorted=True
for i in range(len(arr)-1):
    if arr[i]<=arr[i+1]:
        continue
    else:
        sorted =False
        print('arry is not sorted')
if sorted:
    print('array is sorted')