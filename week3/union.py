num1 = [1,2,3,4]
num2=[1,2,3,5,4,10]
union=[]
j=0
for i in range(len(num1)):
    if num1[i] not in union:
        union.append(num1[i])
for i in range(len(num2)):
    if num2[i] not in union:
        union.append(num2[i]) 
print(union)