# Programming Assignment-3: Email ID

'''
	Question : Assuming that we have some email addresses in the "username@companyname.com" format,
		   please write program to print the company name of a given email address.
	    	   Both user names and company names are composed of letters only.
'''

# Code

s = input().strip()
for i in range(len(s)):
  if s[i] == "@":
    a=i
  elif s[i]==".":
    b=i
print(s[a+1:b])
