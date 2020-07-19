# Programming Assignment-1: Digits

'''
	Question : You are given a number A which contains only digits 0's and 1's.
		   Your task is to make all digits same by just flipping one digit
		   (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the
		   digits same by just flipping one digit then print 'YES' else print 'NO'.
'''

# Code

a=input()
s1=s2=0
for i in a:
   if i=="0":
    s1+=1
   else:
    s2+=1
if s1==1 or s2==1:
  print("YES")
else:
  print("NO")