# Programming Assignment-3: Matrix

'''
	Question : You are provided with the number of rows (R) and columns (C).
		   Your task is to generate the matrix having R rows and C columns
		   such that all the numbers are in increasing order starting from 1 in row wise manner.
'''

# Code

r,c=map(int,input().split())
a=1
for i in range(r):
  for j in range(c):
    if j==c-1:
      print(a)
    else:
      print(a,end=" ")
    a+=1