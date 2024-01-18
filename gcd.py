n1=4
n2=8
for i in range(1,min(n1,n2)+1):
    if(i%n1 == 0 or i%n2 == 0):
        print(i)
    
