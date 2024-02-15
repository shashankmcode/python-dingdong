num = 1, 0, 1, 1, 0, 1
count=0
maxcount=0
for i in range(len(num)):
    if num[i]==1:
        count+=1
        if count>maxcount:
            maxcount=count
    else:
        count=0
print(maxcount)
