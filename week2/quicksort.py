def part(array,low,high):
    start=low
    end=high
    pivot=array[low]
    while start < end:
      while start <= end and array[start]<=pivot:
        start+=1
      while start < end and array[end]>pivot:
        end-=1
    
      if(start < end): #bhai yahan  pe dekh jab start end ke samne chala gaya tab karna hota(swap s,e) varna neeche  
        array[start],array[end]=array[end],array[start]
    
    array[low], array[end] = array[end], array[low]
    return end

    




def quicksort(array, low, high):
    if low < high:
        pi = part(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)
        print(pi)




array = [10, 7, 8, 9, 1, 5]
N = len(array)
quicksort(array, 0, N - 1)
print(array)



""" def part(array, low, high):
    start = low
    end = high
    pivot = array[low]

    while start < end:
        while start <= high and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    # Swap pivot with element at end
    array[low], array[end] = array[end], array[low]

    return end

def quicksort(array, low, high):
    if low < high:
        pi = part(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

array = [10, 7, 8, 9, 1, 5]
N = len(array)
quicksort(array, 0, N - 1)
print(array) 
  """