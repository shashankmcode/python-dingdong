def selection_sort(arr):
    for i in  range(len(arr)-1):
         min=i
         for j in range(i+1,len(arr)):
              if arr[j]<arr[min]:
                   min=j
         arr[i],arr[min]=arr[min],arr[i]


# Test the function
arr = [5,4,3,7,1,6]
print(len(arr))
selection_sort(arr)
print("Sorted array is:", arr)
