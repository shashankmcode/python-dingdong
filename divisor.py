import math
num = 36  # The number for which you want to find the divisors
i = 1

while i <= math.sqrt(num):
    if num % i == 0:
        print(i)
        if(num//i != i):
          print(num//i)
    i += 1
