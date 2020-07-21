# Programming Assignment-1: Formula

'''
	Question : Write a program that calculates and prints the value according to the given formula:

		   Q = Square root of [(2 * C * D)/H]
		   Following are the fixed values of C and H:
		   C is 50. H is 30.
		   D is the variable whose values should be input to your program in a comma-separated sequence.
'''

# Code

a=input().strip()
a=a.replace(","," ")
l=a.split()
l1=[]
for i in l:
  b=((2*50*int(i))/30)**(0.5)
  l1.append(round(b))
print(*l1,sep=",")