# Programming Assignment-1: Digit

'''
	Question : You are provided with a number D containing only digits 0's and 1's.
	    	   Your aim is to convert this number to have all the digits same.
		   For that, you will change exactly one digit i.e. from 0 to 1 or from 1 to 0.
		   If it is possible to make all digits equal (either all 0's or all 1's) by
		   flipping exactly 1 digit then output "YES", else print "NO" (quotes for clarity).
'''

# Code

n=input().strip()
a=n.replace("1","0",1)
s=n.replace("0","1",1)
a=a.replace("1","")
s=s.replace("0","")
if(len(a)==0 or len(s)==0):print("YES")
else:print("NO")