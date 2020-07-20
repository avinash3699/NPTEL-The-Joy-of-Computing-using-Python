# Programming Assignment-2: Symmetric

''' 
	Question: Given a square matrix of N rows and columns, find out whether it is symmetric or not
'''

# Code 

n=int(input());
a=[list(map(int,input().split())) for i in range(n)];
i=0;
symmetric='YES';
while(i<n-1):
  j=i+1;
  while(j<n):
    if(a[i][j]!=a[j][i]):
      symmetric='NO';
      break;
    j+=1;
  i+=1;
print(symmetric,end='');