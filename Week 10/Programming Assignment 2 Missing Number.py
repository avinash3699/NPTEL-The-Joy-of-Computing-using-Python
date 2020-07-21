# Programming Assignment-2: Missing Number

'''
	Question : Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates.
'''

# Code

l=list(map(int,input().split()))
l.sort()
l1= list(range(1,len(l)+2))
for i in l1:
    if i not in l:
         print(i)
         exit()