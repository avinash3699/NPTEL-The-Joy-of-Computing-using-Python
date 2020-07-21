# Programming Assignment-2: First and Last

'''
	Question : Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
		   If the string length is less than 2, return instead of the empty string.
'''

# Code

s=input().strip()
if len(s)<2:
    print("",end="")
else:
    print(s[:2]+s[len(s)-2:len(s)],end="")