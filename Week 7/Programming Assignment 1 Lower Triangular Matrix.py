# Programming Assignment-1: Lower Triangular Matrix

''' 
	Question: Write a program to convert a square matrix into a lower triangular matrix.
'''

# Code 

n=int(input());
a=[list(map(int,input().split())) for i in range(n)];
for i in range(n):
  for j in range(n):
    end = '' if j == n-1 else ' ';
    if(i>=j):                         
      print(a[i][j], end=end);
    else:
      print(0, end=end);
  end = '' if i == n-1 else '\n';
  print('',end=end); 
