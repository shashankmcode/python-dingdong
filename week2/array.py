def swap(arr,start,end):
    if(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        return swap(arr,start+1,end-1)
    print(arr)
arr=[1,2,3,4,5,7]
swap(arr,0,len(arr)-1)