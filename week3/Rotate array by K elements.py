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

""" In the slice notation arr[-k:], the meaning of start, stop, and step can be understood as follows:

start: Since -k is negative, it refers to an index relative to the end of the list arr. Specifically, it indicates the start of the slice. -k means k elements from the end of the list.
stop: The colon : signifies the separation between start and stop. Since : is followed by nothing after it, stop defaults to the end of the list, meaning it will include elements up to the end of the list.
step: Since there's no explicit step specified, it defaults to 1, meaning every element will be included in the slice without skipping an """