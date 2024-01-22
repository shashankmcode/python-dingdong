""" def merge(a,start,end):
    if start<end:
        mid=(start+end)//2
        #print(mid)
        left=a[start:mid+1]   
        right= a[mid+1:end+1]

  #just incase to print the subarray      print(left)   
  #same      print(right)                
        merge(a,start,mid)
        merge(a,mid+1,end)


a = [1,2,3,4,5,6]
#print(len(a))
merge(a,0,len(a)-1)
print("Sorted array is:", a) """

#the above code is just to undeerstand indepth niche full direct likhunga
def merge(a):
 if len(a)>1:
       
    

    left_part=a[:len(a)//2]       #2 6 5 1 7 4 3
    right_part=a[len(a)//2:]

    """ print(left_part)                    #[1, 2, 3]
    print(right_part)   """                # [4, 5, 6]
#recursiom
    merge(left_part)
    merge(right_part)

#merge
    i=0
    j=0
    k=0

    while i<len(left_part) and j<len(right_part):
      if left_part[i]<right_part[j]:
        a[k]=left_part[i]
        i+=1
        k+=1
      else:
        a[k]=right_part[j]
        j+=1
        k+=1

    while i<len(left_part):
      a[k]=left_part[i]
      k+=1
      i+=1

    while j <len(right_part):
      a[k]=right_part[j]
      k+=1
      j+=1


a = [12, -5, 9, -2, 8, 3, -7, 10, 4, -6, 1, 11]
#print(len(a))
merge(a)
print("Sorted array is:", a)