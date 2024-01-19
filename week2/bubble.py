def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
             arr[j],arr[j+1]=arr[j+1],arr[j]
            
arr = [6,5,4,3,2,1]

selection_sort(arr)
print("Sorted array is:", arr)









arr = [5,4,3,2,1]
print(len(arr))
selection_sort(arr)
print("Sorted array is:", arr)