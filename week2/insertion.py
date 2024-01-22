def insertion(arr):
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1



arr = [5,4,3,7,1]
print(len(arr))
insertion(arr)
print("Sorted array is:", arr)