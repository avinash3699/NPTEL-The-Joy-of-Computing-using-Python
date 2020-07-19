# Programming Assignment-2: End-Sort

'''
	Question : Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list.
		   Find the minimum number of moves required to sort the list using this method in ascending order. 

'''

# Code

l=list(map(int,input().split()))
l1=sorted(l)
c=0
for i in range(len(l)):
  if l[i]==l1[c]:
  	c+=1
print(len(l)-c)