# Programming Assignment-2: word-sorting

'''
	Question : Write a program that accepts a comma-separated sequence of words as input and
		   prints the words in a comma-separated sequence after sorting them alphabetically.
'''

# Code

s=input().strip()
l=s.split(",")
print(*sorted(l),sep=",")