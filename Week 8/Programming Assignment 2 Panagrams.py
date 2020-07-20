# Programming Assignment-2: Panagrams

''' 
	Question: A panagram is a sentence containing every 26 letters in the English alphabet.
		  Given a string S, check if it is panagram or not.
'''

# Code 

s=input().strip()
a=[]
for i in s:
  if i.isalpha():
    if i.lower() not in a:
      a.append(i.lower())
if len(a)==26:
  print("YES")
else:
  print("NO")