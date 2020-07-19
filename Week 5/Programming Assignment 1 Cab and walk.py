# Programming Assignment-1: Cab and walk

'''
	Question : Arun is working in an office which is N blocks away from his house. He wants to minimize the time it takes him to go from his house to the office.
		   He can either take the office cab or he can walk to the office.
		   Arun's velocity is V1 m/s when he is walking. The cab moves with velocity V2 m/s but whenever he calls for the cab, it always starts from the office, covers N blocks, collects Arun and goes back to the office.
		   The cab crosses a total distance of N meters when going from office to Arun's house and vice versa, whereas Arun covers a distance of 2–√∗N while walking.
		   Help Arun to find whether he should walk or take a cab to minimize the time.
'''

# Code

n,a,b=map(int,input().split())
c=(2**0.5)*n
d=c/a
x=2*n
y=x/b
if d<y:
  print("Walk")
else:
  print("Cab")