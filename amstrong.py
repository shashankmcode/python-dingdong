num=370
temp=num
sum=0
for i in range(num,0,-1):
    rem=num%10
   # print(rem)
    sum=sum+(rem**3)
    #print(sum)
    num=num//10
if sum == temp:
    print('yes amstrong',sum)
else:
    print('nai he')
    
    
    

