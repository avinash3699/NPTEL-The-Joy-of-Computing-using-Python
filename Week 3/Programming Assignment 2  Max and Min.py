#Programming Assignment-2: Max and Min

'''
	Question : Given a list of numbers (integers), find second maximum and second minimum in this list.
'''

# Code

l=list(map(int,input().split()))
l.sort()
print(l[-2],l[1])