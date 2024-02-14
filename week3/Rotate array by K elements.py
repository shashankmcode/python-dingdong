#most optimal approch
arr = [1, 2, 3, 4, 5]
n = len(arr)
k =11
k%=n
arr[:k]=arr[:k][::-1]
arr[k:]=arr[k:][::-1]
arr=arr[::-1]
print(arr)


#brute force approach
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 11
k %= n
temp = []
if k==0:
    temp=arr.copy()
for i in range(k):
    temp.append(arr[i])

for i in range(k,n):
    arr[i-k]=arr[i]
print(temp)
arr[-k:]=temp
print(arr)

