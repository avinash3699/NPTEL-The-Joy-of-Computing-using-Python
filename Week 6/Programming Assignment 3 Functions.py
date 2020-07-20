# Programming Assignment-3: Functions

'''
	Question : Given an integer number n, define a function named printDict() which can print a dictionary
		   where the keys are numbers between 1 and n (both included) and the values are square of keys.
		   The function printDict() doesn't take any argument.
'''

# Code

def printDict():
  x=int(input())
  d={}
  for i in range(1,x+1):
    d[i]=i**2
  print(d,end='')
                 
printDict()