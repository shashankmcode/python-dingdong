import math
num = 7
i = 1
count=0
while i <= math.sqrt(num):
    if num % i == 0:
        count+=1
        if(num//i != i):
          count+=1
    i += 1
if(count == 2):
   print('yes')
else:
   print('no')