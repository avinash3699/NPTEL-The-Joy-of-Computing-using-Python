# Programming Assignment-3: Rearrangement

'''
	Question : Given a list A of elements of length N, ranging from 1 to N. All elements may not be present in the array.
		   If the element is not present then there will be -1 present in the array.
		   Rearrange the array such that A[i] = i and if i is not present display -1 at that place.
'''

# Code

l=list(map(int,input().split()))
n=len(l)
l1=list(range(0,n))
for i in l1:
    if i in l:
       print(i,end=" ")
    else:
       print(-1,end=" ")