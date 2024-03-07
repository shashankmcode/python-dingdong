n = 4
r = 2
res = 1

for i in range(1, r+1):
    res *= n - (i - 1)
    res //= i

print(res)
