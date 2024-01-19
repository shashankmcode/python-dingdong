def sumof(n, sum=0):
    if n == 0:
        return sum
    else:
        sum = sum + n
        return sumof(n - 1,sum)  # Issue: The updated sum is not being passed to the recursive call
        #return sum  # Issue: This prints the sum without waiting for recursive calls to complete

print(sumof(2))


