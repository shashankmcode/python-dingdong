#brute force(no duplicate elemets)
""" arr=[1,2,3,4,5]
n=len(arr)
print(n)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
         arr[j], arr[j+1] = arr[j+1], arr[j]
print("second smallest element is",arr[1])
print("second largest element is",arr[n-2])
 """
#optimal approcah(duplicate bhi chalega)
""" arr=[1,2,3,5,5]
n=len(arr)
print(n)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
         arr[j], arr[j+1] = arr[j+1], arr[j]
largest=arr[-1]
secondlargest=0
for i in range(n):
   if(arr[i]>secondlargest and arr[i]!=largest):
      secondlargest=arr[i]
print(secondlargest) """

#best approach
arr=[1,2,3,5,5]
n=len(arr)
largest=arr[0]
secondlargest=-1
for i in range(n):
   if arr[i]>largest:
      secondlargest=largest
      largest=arr[i]
   elif arr[i]<largest and arr[i]>secondlargest:
      secondlargest=arr[i]
print(secondlargest)
