# Programming Assignment-2: Factorial

'''
	Question : Given an integer number n, you have to print the factorial of this number.
'''

# Code

a=int(input())
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact,end="")