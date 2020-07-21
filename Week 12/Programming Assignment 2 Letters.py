# Programming Assignment-2: Letters

'''
	Question : Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
'''

# Code

s=input().strip()
u=0;l=0
for i in s:
  if i.isupper():u+=1
  elif i.islower():l+=1
print(u,l)