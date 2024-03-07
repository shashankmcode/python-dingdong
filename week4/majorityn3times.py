#Brute
num=[3,2,3]
temp=[]
n=len(num)
for i in range(n):
    count=0
    for j in range(n):
        if num[i]==num[j]:
            count+=1
            if count>len(num)/3 and num[i] not in temp:
                temp.append(num[i])
                break
print(temp)
