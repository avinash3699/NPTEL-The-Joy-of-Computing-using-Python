# Programming Assignment-3: Multiple of 5

'''
	Question : Given a list A of numbers (integers), you have to print those numbers which are not multiples of 5.
'''

# Code

l=list(map(int,input().split()))
for i in l:
  if i%5!=0:
    print(i,end=" ")