# Programming Assignment-3: Binary Matrix

''' 
	Question: Given a matrix with N rows and M columns, the task is to check if the matrix is a Binary Matrix.
		  A binary matrix is a matrix in which all the elements are either 0 or 1.

'''

# Code 

m,n=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
b='YES'
for i in range(m):
  for j in range(n):
    if(l[i][j]!=0 and l[i][j]!=1):
      b='NO'
      break
  if(b=='NO'):
    break
print(b,end='')