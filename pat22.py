N = 5
for i in range(1, N*2):
    for j in range(1, N*2):
        print(max(N-i+1, N-j+1, i-N+1, j-N+1), end=' ')
    print()
