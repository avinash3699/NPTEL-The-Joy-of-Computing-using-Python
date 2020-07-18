#Programming Assignment-3: Small

'''
	Question : Given two numbers (integers) as input, print the smaller number.
'''

# Code

a,b = map(int,input().split())
if a>b:
  print(b)
else:
  print(a)