matrix=[[1,2,3],[4,5,6],[7,8,9,4]]
n=len(matrix)
m=len(matrix[0])
ans=[[None]*m for _ in range(n)]
print(n,m)
for i in range(n):
    for j in range(m):
        ans[j][n-i-1]=matrix[i][j]
print(matrix)
print(ans)




        
       
