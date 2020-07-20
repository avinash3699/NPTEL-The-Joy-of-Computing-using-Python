# Programming Assignment - 1: Duplicate Elements

''' 
	Question: With a given list L of integers, write a program to print this list L after removing all duplicate values with original order preserved.
'''

# Code 

l = list(map(int,input().split()))
unique_integers = []
for i in l:
    if i not in unique_integers:
        unique_integers.append(i)
print(*unique_integers)
		