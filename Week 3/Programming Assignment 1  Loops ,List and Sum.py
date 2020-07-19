#Programming Assignment-1: Loops ,List and Sum

''' 
	Question : Given an array A of N numbers (integers), you have to write a program
	which prints the sum of the elements of array A with the corresponding elements
	of the reverse of array A.
	If array A has elements [1,2,3], then reverse of the array A will be [3,2,1] and the resultant array should be [4,4,4].
'''

# Code

n=int(input())
l=list(map(int,input().split()))
for i in range(n):
  print(l[i]+l[-(i+1)],end=" ")