#bruteforce woeks for any numbers 
""" matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
n=len(matrix)
m=len(matrix[0])
for i in range(n):
    for j in range(m):
        if matrix[i][j]==0:
            for k in range(n):
                if matrix[k][j]!=0:
                    matrix[k][j]=-1
            for l in range(m):
                if matrix[i][l]!=0:
                    matrix[i][l]=-1
print(matrix)
for i in range(n):
    for j in range(m):
        if matrix[i][j]==-1:
            matrix[i][j]=0

print(matrix) """

#optimized sol
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
n=len(matrix)
m=len(matrix[0])
row=[None]*n
col=[None]*m
for i in range(n):
    for j in range(m):
        if matrix[i][j]==0:
            row[i]=1
            col[j]=1
for i in range(n):
    for j in range(m):
        if(row[i] or col[j]):
            matrix[i][j]=0
print(matrix)



#without using extra spaces
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

n=len(matrix)
m=len(matrix[0])
col=1
for i in range(n):
    for j in range(m):
        if matrix[i][j]==0:
            matrix[i][0]=0 #mark ith rows 0
            if(j!=0):#skip first colum
             matrix[0][j]=0#mark jth col except first colum 0
            else:
                col=0#if 0 in first colum make this 0
for i in range(1,n):
    for j in range(1,m):
        if matrix[i][j]!=0:
           if 0 in (matrix[0][j], matrix[i][0]):
            matrix[i][j]=0
for j in range(m):
    if matrix[0][0]==0:
        matrix[0][j]=0
if col==0:
    for i in range(n):
        matrix[i][0]=0
print(matrix)

""" 
Sure, I’d be happy to explain!

In Python, a 2D list (or matrix) is a list of lists. The outer list represents the rows and each inner list represents a column in that row. Here’s an example of a 2D list:

Python

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
AI-generated code. Review and use carefully. More info on FAQ.
This matrix has 3 rows and 3 columns. You can think of it like a table:

1	2	3
4	5	6
7	8	9
To iterate over the rows and columns of the matrix, you can use nested for loops. The outer loop iterates over each row, and the inner loop iterates over each column in the current row:
matrix[i][0] refers to the first element of the i-th row of the matrix.
matrix[0][j] refers to the j-th element of the first row of the matrix.




Python

for i in range(len(matrix)):       # Iterate over each row
    for j in range(len(matrix[0])):  # Iterate over each column in the current row
        print(matrix[i][j])         # Access the cell at row i, column j
AI-generated code. Review and use carefully. More info on FAQ.
In this code, len(matrix) gives the number of rows and len(matrix[0]) gives the number of columns. matrix[i][j] accesses the cell at row i and column j.

I hope this helps! Let me know if you have any other questions. 😊 """






"""  for k in range(n):
                    print(k)
                #if matrix[i][k]!=-1:
                    matrix[i][k]=-1
            for k in range(n):
                print(k)
                matrix[k][j] = -1 """

            

