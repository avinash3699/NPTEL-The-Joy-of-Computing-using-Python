# Programming Assignment-3: Numbers

'''
	Question : Write a program, which will find all such numbers between m and n
		   (both included) such that each digit of the number is an even number.
'''

# Code

a=input().strip()
m,n=map(int,a.split(","))
l=[]
for i in range(m,n+1):
  i=str(i)
  for j in i:
    if int(j)%2!=0:
      break
  else:
  	l.append(i)
print(*l,sep=",")